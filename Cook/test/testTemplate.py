import json
import sys
import libcook
import pprint

__DEBUG_ENABLE__ = False

_NAME_       = 'name'
_VERSION_    = 'version'
_NODE_ROOT_  = 'menu_nodes'
_JS_DEP_     = 'js_dep'
_TITLE_      = 'title'
_ARG_        = 'arg'
_INDEX_      = 'index'

if __name__ == '__main__':

    menu_file = sys.argv[1]
    present_dir = sys.argv[2]
    present_file = sys.argv[3]
    menu = {}

    with open(menu_file) as fd:
        menu = json.load(fd)

    if __DEBUG_ENABLE__ :
        pprint.pprint(menu)

    result = libcook.parseTemplate(present_dir, present_file, menu)
    libcook.saveTemplate(result, 'output.txt')
