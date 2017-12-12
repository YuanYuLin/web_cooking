import cook_packages as CP
import ops_template

class Package(CP.Angular4Package):
  def gen_app_module_ts(template_file, template_obj):
    output = ops_template.generateTemplateByFile(template_file, template_obj)
    print output

  _properties = {
    "TEMPLATE_FILES":[
      {"name": "app.module.ts", "method": gen_app_module_ts}
    ],
    "NG4_IMPORTS":[
      {"BrowserModule":"@angular/platform-browser"},
      {"NgModule":"@angular/core"}
    ],
    "COOK_DEPS":[
    ]
  }

def main(name, args):
  pkg = Package(name, args)
  return pkg
