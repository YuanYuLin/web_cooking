#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'any':['appConfig']}

def MAIN(name, data, input_dir, output_dir):
    libcook.installPkgHtml(name, data, 'index.html', 'index.html')
    libcook.installPkgCss(name, data, 'app.css', 'app.css')

def MAIN_INSTALL(name, data):
    libcook.installAppHtml(name, data, 'index.html', 'index.html')
    libcook.installAppCss(name, data, 'app.css', 'app.css')

