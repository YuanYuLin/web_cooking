#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'any':['angularjs']
            }

def MAIN(name, data, input_dir, output_dir):
    libcook.installPkgJs(name, data, 'app.config.js', 'app.config.js')

def MAIN_INSTALL(name, data):
    libcook.installAppJs(name, data, 'app.config.js', 'app.config.js')

