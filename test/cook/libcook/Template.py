from jinja2 import Environment, FileSystemLoader
import os
import shutil
import sys
import pprint

def ossep():
    return os.sep

def debug(obj):
    print "===DEBUG==="
    pprint.pprint(obj)
    print "============"

def includespices(name):
    return 'spices' + os.sep + name + '.cook'

def bugon(file_name, msg):
    print "Please check " + file_name + "!!"
    print "BUGON:( " + msg + " )"
    sys.exit(1)

def parseTemplate(template_dir, template_name, project_data):
    env = Environment(loader=FileSystemLoader(template_dir))
    env.globals['OSSEP'] = ossep()
    env.globals['SPICES'] = includespices
    env.globals['BUGON'] = bugon
    env.globals['DEBUG'] = debug
    print "(----------------------------)"
    pprint.pprint(project_data)
    print "[===========================]"
    result = env.get_template(template_name).render(project_data)
    return result

def saveTemplate(templateResult, output_dir, output_file):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    w_path = output_dir + os.sep + output_file
    with open(w_path, 'w') as fd:
        fd.write(templateResult)

def parseAndSaveTemplate(in_tmpl_dir, in_tmpl_name, out_dir, out_name, data):
    result = parseTemplate(in_tmpl_dir, in_tmpl_name, data)
    saveTemplate(result, out_dir, out_name)

def copyFile2File(in_dir, in_file_name, out_dir, out_file_name):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    shutil.copyfile(in_dir + os.sep + in_file_name, out_dir + os.sep + out_file_name)
