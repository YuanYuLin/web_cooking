#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'simple':['simple'],
            'dashboardMD':['dashboardMD', 'libCore'],
            'dashboardMDL':['dashboardMDL', 'libCore'],
            'any':[]}

def MAIN(name, data, input_dir, output_dir):
    libcook.installPkgHtml(name, data, 'view.html', name + '.html')
    libcook.installPkgJs(name, data, 'view.component.js', name + '.component.js')

def MAIN_INSTALL(name, data):
    libcook.installAppHtml(name, data, name + '.html', name + '.html')
    libcook.installAppJs(name, data, name + '.component.js', name + '.component.js')

