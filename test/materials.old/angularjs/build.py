#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'any':[]}

def MAIN(name, data, input_dir, output_dir):
    libcook.installBowerPkgs(name, data, {"angular":"~1.6.0", "angular-route":"~1.6.0"})

def MAIN_INSTALL(name, data):
    libcook.installAppJs(name, data, 'angular' + os.sep + 'angular.min.js', 'angular.min.js')
    libcook.installAppJs(name, data, 'angular-route' + os.sep + 'angular-route.min.js', 'angular-route.min.js')

