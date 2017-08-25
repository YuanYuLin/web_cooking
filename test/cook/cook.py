#!/usr/bin/python2.7
import sys
import libcook
import os
import pprint
import imp
import subprocess
import json
from operator import itemgetter

def usage():
    print "cook.py <material_pool> <output_food> <menu> <action>"

def run_action(action, data):

    if action == "RUN" :
        out_pkg_dir = data[libcook.R_FOOD_APP_DIR]
        libcook.execCmd(['npm', 'start'], out_pkg_dir)
        sys.exit(0)

    if action == "ALL" :
        for material in libcook.orderPackages(data):
            libcook.buildMaterialPkg(data, material['name'])
            libcook.installMaterialPkg(data, material['name'])

    if action == "BUILD" :
        for material in libcook.orderPackages(data):
            libcook.buildMaterialPkg(data, material['name'])

    if action == "INSTALL" :
        for material in  libcook.orderPackages(data):
            libcook.installMaterialPkgs(data, material['name'])

    if action == "DEP" :
        pprint.pprint(libcook.orderPackages(data))

if __name__ == '__main__':
    if(len(sys.argv) < 5):
        usage()
        sys.exit()

    materials_dir = sys.argv[1]
    output_food_dir = sys.argv[2]
    menu_file = sys.argv[3]
    action = sys.argv[4]
    materials_file = materials_dir + os.sep + 'config.cook'
    data_json = output_food_dir + os.sep + 'data.json'

    libcook.installDevPkgs(output_food_dir)

    data = {}

    if os.path.exists(data_json):
        with open(output_food_dir + os.sep + 'data.json', 'r') as fp:
            data = json.load(fp)

    data[libcook.R_MENU] = libcook.loadJson2Obj(menu_file)

    libcook.data_init(data, materials_dir, output_food_dir)

    run_action(action, data)

    with open(data_json, 'w') as fp:
        json.dump(data, fp)

