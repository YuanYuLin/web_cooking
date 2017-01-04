#!/usr/bin/pyton2.7
import pprint
import os
import libcook
import subprocess

def MAIN_DEPPKG(name, data):
    return {'any':[]}

def printDebugData(data):
    print "====================================="
    #pprint.pprint(data)
    print "====================================="

def MAIN(name, data, input_dir, output_dir):
    printDebugData(data)

def MAIN_INSTALL(name, data):
    gulp_list = []
    pkgs_dep_info = data[libcook.R_MATERIALS_PKGS_DEP]
    for pkg_info in pkgs_dep_info:
        print "pkginfo " 
        pprint.pprint(pkg_info)
        if 'js_seq' in pkg_info :
            for js_dep in pkg_info['js_seq']:
                print js_dep
                gulp_list.append(js_dep)

    data['GULPFILE'] = gulp_list
    materials_dir = libcook.getDirMaterials(data, 'gulp')
    prj_dir = libcook.getDirPrj(data, 'gulp')

    in_name= name + os.sep + "gulp" + os.sep + 'gulpfile.js'
    out_name = 'gulpfile.js'
    libcook.parseAndSaveTemplate(materials_dir, in_name, prj_dir, out_name, data)

    in_name= name + os.sep + "gulp" + os.sep + "package.json"
    out_name = 'package.json'
    libcook.parseAndSaveTemplate(materials_dir, in_name, prj_dir, out_name, data)

    libcook.execCmd(['npm', 'install'], prj_dir)
    libcook.execCmd(['gulp'], prj_dir)

    #proc=subprocess.Popen(['npm', 'start'], cwd=out_pkg_dir)
    #proc.wait()
