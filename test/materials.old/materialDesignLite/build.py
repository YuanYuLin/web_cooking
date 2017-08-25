#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'any':[]}

def MAIN(name, data, input_dir, output_dir):
    libcook.installBowerPkgs(name, data, {"material-design-lite" : "^1.2.1"})

def MAIN_INSTALL(name, data):
    libcook.installAppJs(name, data, 'material-design-lite' + os.sep + 'material.min.js', 'material.min.js')

    pkg_js_dir = libcook.getDirPrjPkgJs(data, name)
    app_css_dir = libcook.getDirPrjAppCss(data, name)
    libcook.copyFile2File(pkg_js_dir, 'material-design-lite' + os.sep + 'material.min.css' , app_css_dir, 'material.min.css')

