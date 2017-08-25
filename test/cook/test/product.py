#!/usr/bin/python2.7
import os
import sys
import subprocess

def usage():
    print "product.py <folder>"
    sys.exit()

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        usage()

    pristine_dir = os.path.realpath(sys.argv[1])

    proc=subprocess.Popen(['bower', 'install'], cwd=pristine_dir)
    proc.wait()
