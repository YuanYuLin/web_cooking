from cook_packages import Loader

class LoaderImp(Loader):
  def _is_debug(self):
    return True

  def do_make(self):
    self.pkg_list_make()

  def do_deps(self):
    self.travel_pkgs(self.pkg_sort_deps)
    self.show_pkgs()

def _make(args):
  loader = LoaderImp(args)
  loader.do_deps()
  loader.do_make()

def _deps(args):
  loader = LoaderImp(args)
  loader.do_deps()

ActionTable = {
"DEPS": _deps,
"MAKE": _make,
}

