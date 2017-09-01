from cook_packages import Loader

class LoaderImp(Loader):
  _dep_list = {"pkg_name":"", "priority":0}

  def _is_debug(self):
    return True

  def run(self):
    super(LoaderImp, self).run()

  def do_deps(self):
    super(LoaderImp, self, dep_list

def _make(args):
  loader = LoaderImp(args)
  loader.run()

def _deps(args):
  loader = LoaderImp(args)
  loader.do_deps()

ActionTable = {
"DEPS": _deps,
"MAKE": _make,
}

