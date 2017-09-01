import pprint
import ops

#'''
#  ----------      -------------------
#  | Loader | *--> | Angular4Package |
#  ----------      -------------------
#'''
class Package(object):
  _args = None
  def __init__(self, args):
    self._args = args

#
#
#
#
class Angular4Package(Package):
  NG_IMPORTS="ng_imports"
  COOK_DEPS="cook_deps"
  _properties = {"NG4_IMPORTS":[], "COOK_DEPS":[]}

  def get_ng4_imports(self):
    return self._properties["NG4_IMPORTS"]

  def get_cook_deps(self):
    return self._properties["COOK_DEPS"]

#
# Used to load package
# 
#
#
class Loader(object):
  _args = None
  #_pkgs = [{"name":"", "instance":None, "dep_count":0]
  _pkgs = []

  def __init__(self, args):
    self._args = args

  def do_deps(self, dep_list):
    print dep_list

  def launch_pkg(self, pkg_name):
    pkg_found = False
    for pkg in self._pkgs:
      if pkg.name == pkg_name:
        pkg_found = True
        break

    if pkg_found:
      print ""
    else:
      module_path = ops.path_join(self.get_materials(), pkg_name)
      launch_script = "pkg"
      py_script = ops.loadModule(pkg_name, launch_script, [module_path])
      pkg_obj = py_script.main(self._args)

      pprint.pprint(pkg_obj.get_cook_deps())

  def run(self):
    self.debug()
    menu = self.get_menu()
    packages = menu['packages']
    for pkg in packages:
      pkg_enabled = pkg['enabled']
      pkg_name = pkg['name']
      if pkg_enabled:
        self.launch_pkg(pkg_name)

  def debug(self):
    if self._is_debug():
      self.show_args()
      self.show_menu()
      self.show_materials()
      self.show_food()
      self.show_action()

  def show_args(self):
    print "args:"
    pprint.pprint(self._args)

  def get_menu(self):
    return ops.loadJson2Obj(self._args['menu'])

  def show_menu(self):
    print "menu:"
    menu = self.get_menu()
    pprint.pprint(menu)

  def get_materials(self):
    return self._args['materials']

  def show_materials(self):
    print "materials"
    materials = self.get_materials()
    pprint.pprint(materials)

  def get_food(self):
    return self._args['food']

  def show_food(self):
    print "food"
    food = self.get_food()
    pprint.pprint(food)

  def get_action(self):
    return self._args['action']

  def show_action(self):
    print "action"
    action = self.get_action()
    pprint.pprint(action)

