import pprint
import ops
from operator import itemgetter
from bottle import SimpleTemplate

#'''
#  ----------      -------------------
#  | Loader | *--> | Angular4Package |
#  ----------      -------------------
#'''
class Package(object):
  _args = None
  _name = ""
  _priority = 0
  _template_name = ""
  _template_output_file = ""
  def __init__(self, name, args):
    self._args = args
    self._name = name

  def upgrade_priority(self):
    self._priority += 1

  def get_pkg_name(self):
    return self._name

  def get_pkg_priority(self):
    return self._priority

  '''
  def generate_template(self, tmpl_obj, output_dir):
    #pprint.pprint(tmpl_obj)
    tmpl = SimpleTemplate(name=self._template_name)
    output = tmpl.render(tmpl_obj)
    return output
    print ops.path_join(output_dir, self._template_output_file)
    with open(ops.path_join(output_dir, self._template_output_file), 'w') as fp:
      fp.write(output)
  '''
#
#
#
#
class Angular4Package(Package):
  NG_IMPORTS="ng_imports"
  COOK_DEPS="cook_deps"
  _properties = {"NG4_IMPORTS":[], "COOK_DEPS":[], "TEMPLATE_FILES":[], "TEMPLATE_COMMON_PATH":""}

  def get_ng4_imports(self):
    return self._properties["NG4_IMPORTS"]

  def get_cook_deps(self):
    return self._properties["COOK_DEPS"]

  def get_templates(self):
    if "TEMPLATE_FILES" in self._properties:
      return self._properties["TEMPLATE_FILES"]
    return []

  def generate_templates(self):
    self._properties["TEMPLATE_COMMON_PATH"] = ops.path_join(self._args['materials'], 'common')
    for tmpl in self.get_templates():
      tmpl_full_name = ops.path_join(ops.path_join(self._args['materials'], self._name), tmpl["name"])
      method = tmpl["method"]
      method(tmpl_full_name, self._properties)

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

  def get_pkg_priority_list(self):
    #_dep_list = {"pkg_name":"", "priority":0}
    _dep_list = []
    for pkg_obj in self._pkgs:
      pkg = pkg_obj["instance"]
      _dep_list.append({"pkg_name":pkg.get_pkg_name(), "priority":pkg.get_pkg_priority()})
    return sorted(_dep_list, key=itemgetter('priority'), reverse=True)

  def show_pkgs(self):
    print "PKGS:"
    for pkg_obj in self.get_pkg_priority_list():
      print pkg_obj

  def get_pkg_obj(self, pkg_name):
    isFound = False
    pkg_obj = None
    for pkg in self._pkgs:
      if pkg["name"] == pkg_name:
        pkg_obj = pkg["instance"]
        isFound = True
        break
    if isFound:
      print "Found:", pkg_name
    else:
      module_path = ops.path_join(self.get_materials(), pkg_name)
      launch_script = "pkg"
      py_script = ops.loadModule(pkg_name, launch_script, [module_path])
      pkg_obj = py_script.main(pkg_name, self._args)
      self._pkgs.append({"name":pkg_name, "instance":pkg_obj})

    return pkg_obj

  def travel_pkgs(self, call_back):
    menu = self.get_menu()
    packages = menu['packages']
    for pkg in packages:
      pkg_obj = None
      pkg_enabled = pkg['enabled']
      pkg_name = pkg['name']
      #print pkg_name, pkg_enabled
      if pkg_enabled:
        pkg_obj = self.get_pkg_obj(pkg_name)
        call_back(pkg_obj)

  def pkg_sort_deps(self, pkg_obj):
    pkg_obj.upgrade_priority()
    for pkg_dep in pkg_obj.get_cook_deps():
      dep_pkg_obj = self.get_pkg_obj(pkg_dep['name'])
      self.pkg_sort_deps(dep_pkg_obj)

  def pkg_list_make(self):
    print "PKGS make:"
    for pkg_meta in self.get_pkg_priority_list():
      pkg_obj = self.get_pkg_obj(pkg_meta["pkg_name"])
      pkg_obj.generate_templates()

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

