#!/usr/bin/python2.7
import sys
import os

def help():
    import cook_action
    print "cook.py <materials_dir> <menu_dir> <output_dir> <Action>"
    print "  Action:"
    for act in cook_action.ActionTable:
        print "    " + act
    sys.exit(1)

def setLibPath():
    # append library path
    python_lib = os.path.abspath("pylib")
    #sys.path.append(python_lib)

    if not os.path.exists(python_lib):
        print "Please download [pylib] from github!!"
        print "git clone https://github.com/YuanYuLin/pylib.git"
        sys.exit(1)

    sys.path.append(python_lib)
    python_lib = os.path.abspath("pycook")
    sys.path.append(python_lib)

if __name__ == '__main__':
    setLibPath()

    if len(sys.argv) < 5:
        help()

    materials_dir = sys.argv[1]
    menu_file     = sys.argv[2]
    output_dir    = sys.argv[3]
    action        = sys.argv[4]

    print "cook.py", materials_dir, menu_file, output_dir, action

    import cook_action
    if action not in cook_action.ActionTable:
        help()

    args = {"menu":menu_file, "materials":materials_dir, "food":output_dir, "action":action}
    cook_action.ActionTable[action](args)

