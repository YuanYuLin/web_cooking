import cook_packages as CP

class Package(CP.Angular4Package):
  _properties = {
    "NG4_IMPORTS":[
      {"BrowserModule":"@angular/platform-browser"},
      {"NgModule":"@angular/core"}
    ],
    "COOK_DEPS":[
    ]
  }

def main(args):
  pkg = Package(args)
  return pkg
