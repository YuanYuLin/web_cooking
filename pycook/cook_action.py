from cook_packages import Loader

class LoaderImp(Loader):

  def _is_debug(self):
    return True

  def run(self):
    super(LoaderImp, self).run()

def _make(args):
  loader = LoaderImp(args)
  loader.run()

ActionTable = {
"MAKE": _make,
}

