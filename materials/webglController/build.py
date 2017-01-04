#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'simple':['libCore'],
            'dashboard':['angularjs', 'libCore'],
            'any':[]}

def MAIN(name, data, input_dir, output_dir):
    libcook.installPkgJs(name, data, 'view.component.js', name + '.component.js')

def MAIN_INSTALL(name, data):
    libcook.installAppJs(name, data, name + '.component.js', name + '.component.js')

