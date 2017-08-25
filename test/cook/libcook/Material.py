from jinja2 import Environment, FileSystemLoader
import os

def parseMaterial(materials_dir, material_name, project_data, material_data):
    material_dir = materials_dir + os.sep + material_name
    project_data[material_name] = material_data
    env = Environment(loader=FileSystemLoader(material_dir))
    result = env.get_template(material_name).render(project_data)
    return result

def saveTemplate(templateResult, output_file):
    with open(output_file, 'w') as fd:
        fd.write(templateResult)
