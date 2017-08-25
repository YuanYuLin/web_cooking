#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'any':[]}

def MAIN(name, data, input_dir, output_dir):
    libcook.installBowerPkgs(name, data, {"threejs":"http://threejs.org/build/three.min.js"})

def MAIN_INSTALL(name, data):
    libcook.installAppJs(name, data, 'threejs' + os.sep + 'index.js', 'three.js')

