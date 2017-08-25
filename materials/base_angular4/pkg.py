import cook_packages

class Package(cook_packages.Angular4Package):
  _properties = {
    "imports":[
      {"BrowserModule":"@angular/platform-browser"},
      {"NgModule":"@angular/core"}
    ],
    "pkg_deps":[
    ]
  }

def main(args):
  pkg = Package(args)
  return pkg
