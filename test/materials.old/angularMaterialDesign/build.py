#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'any':['angularjs']}

def MAIN(name, data, input_dir, output_dir):
    libcook.installBowerPkgs(name, data, {"angular-material":"~1.1.0"})

def MAIN_INSTALL(name, data):
    print "TEST"
    libcook.installAppJs(name, data, 'angular-animate' + os.sep + 'angular-animate.min.js', 'angular-animate.min.js')
    libcook.installAppJs(name, data, 'angular-aria' + os.sep + 'angular-aria.min.js', 'angular-aria.min.js')
    libcook.installAppJs(name, data, 'angular-material' + os.sep + 'angular-material.min.js', 'angular-material.min.js')

    pkg_js_dir = libcook.getDirPrjPkgJs(data, name)
    app_css_dir = libcook.getDirPrjAppCss(data, name)
    libcook.copyFile2File(pkg_js_dir, 'angular-material' + os.sep + 'angular-material.min.css' , app_css_dir, 'angular-material.min.css')

