#!/usr/bin/pyton2.7
import pprint
import os
import libcook
import subprocess

def MAIN_DEPPKG(name, data):
    return {'any':[]}

def printDebugData(data):
    print "====================================="
    #pprint.pprint(data)
    print "====================================="

def MAIN(name, data, input_dir, output_dir):
    libcook.installNpmPkgs(name, data, [])
    printDebugData(data)

def MAIN_INSTALL(name, data):
    print "-------------------------------------"

