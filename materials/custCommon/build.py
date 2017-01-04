#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'any':['angularjs', 'libCore']}

def MAIN(name, data, input_dir, output_dir):
    libcook.installPkgJs(name, data, 'view.component.js', name + '.component.js')

def MAIN_INSTALL(name, data):
    libcook.installAppJs(name, data, name + '.component.js', name + '.component.js')

