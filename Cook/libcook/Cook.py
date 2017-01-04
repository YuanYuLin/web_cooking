import sys
import libcook
import os
import pprint
import imp
import subprocess
import json
from operator import itemgetter

def data_init(data, materials_dir, output_food_dir):
    if not os.path.exists(output_food_dir):
        os.mkdir(output_food_dir)
    materials_file = materials_dir + os.sep + 'config.cook'
    proj_data = data[libcook.R_MENU]
    materials_data = libcook.loadJson2Obj(materials_file)

    #for build_component in proj_data['build_components']:
    #    for material in materials_data["materials"]:
    #        if build_component["name"] == material["name"]:
    #            build_component["type"] = material["type"]

    data[libcook.R_MATERIALS_DIR] = os.path.abspath(materials_dir)
    data[libcook.R_MATERIALS_PKGS] = materials_data
    data[libcook.R_MATERIALS_PKGS_DEP] = []

    data[libcook.R_FOOD_DIR] = os.path.abspath(output_food_dir)
    data[libcook.R_FOOD_APP_DIR] = os.path.abspath(output_food_dir + os.sep + 'app')
    data[libcook.R_FOOD_PKGS] = []
    data[libcook.R_FOOD_PKGS_DIR] = os.path.abspath(output_food_dir + os.sep + 'pkgs')
    data[libcook.R_FOOD_BOWER_DEPS] = []
    data[libcook.R_FOOD_NODE_DEPS] = []
    data[libcook.R_FOOD_INCLUDES_JS] = []
    data[libcook.R_FOOD_INCLUDES_CSS] = []

def getPkgsDep(data, material_name):
    food_dir = data[libcook.R_FOOD_DIR]
    food_pkgs = data[libcook.R_FOOD_PKGS]
    food_pkgs_dir = data[libcook.R_FOOD_PKGS_DIR]
    materials_dir = data[libcook.R_MATERIALS_DIR]
    pkgs_dep = data[libcook.R_MATERIALS_PKGS_DEP]
    pkg_found = False
    material_not_found = True

    material_dir = materials_dir + os.sep + material_name
    #print material_dir
    imp_fp, imp_pathname, imp_description = imp.find_module('build', [material_dir])
    build_pkg = imp.load_module('buildDeps', imp_fp, imp_pathname, imp_description)
    all_list = build_pkg.MAIN_DEPPKG(material_name, data)
    #print('PKG_NAME:' + material_name)
    #pprint.pprint(all_list)
    pkgs = []
    present_name = data[libcook.R_MENU]['present']
    if present_name in all_list :
        pkgs = all_list[present_name]
    else :
        pkgs = all_list['any']

    if len(pkgs) != 0:
        for pkg in pkgs:
            getPkgsDep(data, pkg)

    for pkg in pkgs_dep:
        if pkg['name'] == material_name:
            pkg_found = True
            break;

    #print "----------------"
    #pprint.pprint(data[libcook.R_MATERIALS_PKGS]["materials"])
    #print "=============="
    if pkg_found :
        pkg['order'] += 1
    else:
        if material_name.startswith('spices'):
            pkgs_dep.append({"name":material_name, "order":0})
        else:
            for material in data[libcook.R_MATERIALS_PKGS]["materials"]:
                print material
                if material["name"] == material_name :
                    pkgs_dep.append({"name":material_name, "order":1, "type": material["type"]})
                    material_not_found = False
                    break

            if material_not_found:
                print "Can NOT find the Material:[" + material_name + "] in config.cook!"
                sys.exit(1)

def orderPackages(data):
    for material in data[libcook.R_MENU]['build_components']:
        getPkgsDep(data, material['name'])

    for material in data[libcook.R_MATERIALS_PKGS_DEP]:
        getPkgsDep(data, material['name'])

    return sorted(data[libcook.R_MATERIALS_PKGS_DEP], key=itemgetter('order'), reverse=True)

def buildMaterialPkg(data, material_name):
    food_dir = data[libcook.R_FOOD_DIR]
    food_pkgs = data[libcook.R_FOOD_PKGS]
    food_pkgs_dir = data[libcook.R_FOOD_PKGS_DIR]
    materials_dir = data[libcook.R_MATERIALS_DIR]

    print "Building " + material_name + "..."
    material_dir = materials_dir + os.sep + material_name
    imp_fp, imp_pathname, imp_description = imp.find_module('build', [material_dir])
    build_pkg = imp.load_module('buildComponent', imp_fp, imp_pathname, imp_description)
    build_pkg.MAIN(material_name, data, materials_dir, food_pkgs_dir + os.sep + material_name)
    food_pkgs.append({'name':material_name})

def installMaterialPkg(data, material_name):
    food_dir = data[libcook.R_FOOD_DIR]
    food_pkgs = data[libcook.R_FOOD_PKGS]
    food_pkgs_dir = data[libcook.R_FOOD_PKGS_DIR]
    materials_dir = data[libcook.R_MATERIALS_DIR]

    print "Installing " + material_name + "..."
    material_dir = materials_dir + os.sep + material_name
    imp_fp, imp_pathname, imp_description = imp.find_module('build', [material_dir])
    build_pkg = imp.load_module('installComponent', imp_fp, imp_pathname, imp_description)
    build_pkg.MAIN_INSTALL(material_name, data)

