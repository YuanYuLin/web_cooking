import ops_template
import ops

def generate_import_header(template_obj):
  template_common_path = ops.path_join(template_obj['TEMPLATE_COMMON_PATH'], "import_header.tmpl")
  return ops_template.generateTemplateByFile(template_common_path, template_obj)
