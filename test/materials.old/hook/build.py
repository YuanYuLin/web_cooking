#!/usr/bin/pyton2.7
import pprint
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'simple':['simple'],
            'dashboard':['dashboard'],
            'any':['']}

def MAIN(name, data, input_dir, output_dir):
    libcook.installPkgHtml(name, data, 'hook.html', 'hook.html')
    libcook.installPkgJs(name, data, 'hook.js', 'hook.js')

def MAIN_INSTALL(name, data):
    libcook.installAppHtml(name, data, 'hook.html', 'hook.html')
    libcook.installAppJs(name, data, 'hook.js', 'hook.js')

