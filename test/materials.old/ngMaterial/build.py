#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'any':['angularMaterialDesign']}

def MAIN(name, data, input_dir, output_dir):
    print ''

def MAIN_INSTALL(name, data):
    pkg_js_dir = libcook.getDirPrjPkgJs(data, 'angularMaterialDesign')
    app_css_dir = libcook.getDirPrjAppCss(data, name)
    app_js_dir = libcook.getDirPrjAppJs(data, name)
    libcook.copyFile2File(pkg_js_dir, 'angular-material' + os.sep + 'angular-material.min.css' , app_css_dir, 'angular-material.min.css')
    libcook.copyFile2File(pkg_js_dir, 'angular-material' + os.sep + 'angular-material.min.js' , app_js_dir, 'angular-material.min.js')

