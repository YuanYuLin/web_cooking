import subprocess
import imp
import sys
import os

def execCmd(cmd_list, work_dir):
    if os.name == "nt":
        proc=subprocess.Popen(cmd_list, cwd=work_dir, shell=True)
    else:
        proc=subprocess.Popen(cmd_list, cwd=work_dir)
        proc.wait()

def checkCmd(cmd_list):
    if os.name == "nt":
        subprocess.check_call(cmd_list, shell=True)
    else:
        subprocess.check_call(cmd_list)
'''
def installJinJa2(work_dir):
    print "Checking Jinja2 ..."
    try:
        imp.find_module('jinja2')
    except:
        try:
            execCmd(['pip', 'install', 'jinja2'], work_dir)
        except:
            print "Jinja2 install failed..."
            sys.exit(1)
'''
def installGit(work_dir):
    print "Check Git ..."
    try:
        devnull = open(os.devnull)
        subprocess.Popen(['git'], stdout=devnull, stderr=devnull).communicate()
    except:
        print "Please download!!"
        print "Git "
        print "https://git-scm.com/download/win"
        sys.exit(1)

def installNodeJs(work_dir):
    print "Checking NodeJs ..."
    try:
        devnull = open(os.devnull)
        subprocess.Popen(['node'], stdout=devnull, stderr=devnull).communicate()
    except:
        print "Please download!!"
        print "NodeJs - v6.9.2 LTS"
        print "https://nodejs.org/en/"
        sys.exit(1)

def installBower(work_dir):
    print "Checking Bower ..."
    try:
        checkCmd(['bower', '-v'])
        print "Bower Installed..."
    except:
        print "Downloading bower ..."
        try:
            execCmd(['npm', 'install', '-g', 'bower'], work_dir)
        except:
            print "NPM download failed..."
            print "Please check PATH of enviroment!"
            print os.environ
            sys.exit(1)

def installGulp(work_dir):
    print "Checking Gulp ..."
    try:
        checkCmd(['gulp', '-v'])
        print "Gulp Installed..."
    except:
        print "Downloading Gulp ..."
        try:
            execCmd(['npm', 'install', '-g', 'gulp'], work_dir)
        except:
            print "NPM download failed..."
            print "Please check PATH of enviroment!"
            print os.environ
            sys.exit(1)

def installHttpServer(work_dir):
    print "Checking Http-server ..."
    try:
        devnull = open(os.devnull)
        subprocess.Popen(['http-server'], stdout=devnull, stderr=devnull).communicate()
        print "Http-server installed..."
    except:
        print "Downloading Http-server ..."
        try:
            execCmd(['npm', 'install', '-g', 'http-server'], work_dir)
        except:
            print "NPM download failed..."
            print "Please check PATH of enviroment!"
            print os.environ
            sys.exit(1)

def installDevPkgs(work_dir):
    #installJinJa2(work_dir)
    installGit(work_dir)
    installNodeJs(work_dir)
    installBower(work_dir)
    installGulp(work_dir)
    installHttpServer(work_dir)
