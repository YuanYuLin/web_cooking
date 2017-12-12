import cook_packages as CP

class Package(CP.Angular4Package):
  _properties = {
    "NG4_IMPORTS":[
      {"BrowserModule":"@angular/platform-browser"},
      {"NgModule":"@angular/core"}
    ],
    "COOK_DEPS":[
      {"name":"base_angular4"}
    ]
  }

def main(name, args):
  pkg = Package(name, args)
  return pkg
