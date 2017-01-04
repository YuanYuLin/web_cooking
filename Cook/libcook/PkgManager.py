import os
import pprint
import subprocess
import Template
R_MENU              = 'MENU'

R_MATERIALS_DIR     = 'MATERIALS_DIR'
R_MATERIALS_PKGS    = 'MATERIALS_PKGS'
R_MATERIALS_PKGS_DEP= 'MATERIALS_PKGS_DEP'

R_FOOD_DIR          = 'FOOD_DIR'
R_FOOD_APP_DIR      = 'FOOD_APP_DIR'
R_FOOD_PKGS         = 'FOOD_PKGS'
R_FOOD_PKGS_DIR     = 'FOOD_PKGS_DIR'
R_FOOD_BOWER_DEPS   = 'FOOD_BOWER_DEPS'
R_FOOD_NODE_DEPS    = 'FOOD_NODE_DEPS'
R_FOOD_INCLUDES_JS  = 'FOOD_INCLUDEJS'
R_FOOD_INCLUDES_CSS = 'FOOD_INCLUDECSS'

def cleanBowerPkg(data):
    data[R_FOOD_BOWER_DEPS] = []

def addBowerPkg(data, name, version):
    bower_deps = data[R_FOOD_BOWER_DEPS]
    bower_deps.append({'name':name, 'version':version})

def cleanNodePkg(data):
    data[R_FOOD_NODE_DEPS] = []

def cleanNodePkg(data):
    data[R_FOOD_NODE_DEPS] = []

def addNodePkg(data, name, version):
    node_deps = data[R_FOOD_NODE_DEPS]
    node_deps.append({'name':name, 'version':version})

def cleanIncludeCssFile(data):
    data[R_FOOD_INCLUDES_CSS] = []

def addIncludeCssFile(data, path):
    include = data[R_FOOD_INCLUDES_CSS]
    include.append(path)

def cleanIncludeJsFile(data):
    data[R_FOOD_INCLUDES_JS] = []

def addIncludeJsFile(data, path):
    include = data[R_FOOD_INCLUDES_JS]
    include.append(path)

def getDirMaterials(data, name):
    return data[R_MATERIALS_DIR]

def getDirPrj(data, name):
    return data[R_FOOD_DIR]

# Material Folder
def getDirMaterial(data, name):
    return data[R_MATERIALS_DIR] + os.sep + name

def getDirMaterialJs(data, name):
    return data[R_MATERIALS_DIR] + os.sep + name + os.sep + 'js'

def getDirMaterialCss(data, name):
    return data[R_MATERIALS_DIR] + os.sep + name + os.sep + 'css'

def getDirMaterialHtml(data, name):
    return data[R_MATERIALS_DIR] + os.sep + name + os.sep + 'html'

def getDirMaterialImage(data, name):
    return data[R_MATERIALS_DIR] + os.sep + name + os.sep + 'images'

# Pkg Folder
def getDirPrjPkg(data, name):
    return data[R_FOOD_PKGS_DIR] + os.sep + name

def getDirPrjPkgJs(data, name):
    return data[R_FOOD_PKGS_DIR] + os.sep + name + os.sep + 'js'

def getDirPrjPkgCss(data, name):
    return data[R_FOOD_PKGS_DIR] + os.sep + name + os.sep + 'css'

def getDirPrjPkgHtml(data, name):
    return data[R_FOOD_PKGS_DIR] + os.sep + name

def getDirPrjPkgImage(data, name):
    return data[R_FOOD_PKGS_DIR] + os.sep + name + os.sep + 'images'

# App Folder
def getDirPrjApp(data, name):
    return data[R_FOOD_APP_DIR] 

def getDirPrjAppJs(data, name):
    return data[R_FOOD_APP_DIR] + os.sep + 'js'

def getDirPrjAppCss(data, name):
    return data[R_FOOD_APP_DIR] + os.sep + 'css'

def getDirPrjAppHtml(data, name):
    return data[R_FOOD_APP_DIR]

def getDirPrjAppImages(data, name):
    return data[R_FOOD_APP_DIR] + os.sep + 'images'

def execCmd(cmd_list, work_dir):
    if os.name == "nt":
        proc=subprocess.Popen(cmd_list, cwd=work_dir, shell=True)
    else:
        proc=subprocess.Popen(cmd_list, cwd=work_dir)
    proc.wait()

def checkCmd(cmd_list):
    if os.name == "nt":
        subprocess.check_call(cmd_list, shell=True)
    else:
        subprocess.check_call(cmd_list)

def installNpmPkgs(name, data, npm_pkgs):
    materials_dir = getDirMaterials(data, name)

    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    pkgs_info = data[R_MATERIALS_PKGS_DEP]
    for pkg_info in pkgs_info:
        if pkg_info['name'] == name :
            if 'npm' in pkg_info :
                print "bower exist!"
            else:
                pkg_info['npm'] = []

            for npm_pkg in npm_pkgs:
                pkg_info['npm'].append({'name':str(npm_pkg), 'version':str(npm_pkgs[npm_pkg])})

            #pprint.pprint(pkg_info)
            Template.parseAndSaveTemplate(materials_dir, name + os.sep + 'package.json', pkg_dir, 'package.json', pkg_info)
            execCmd(['npm', 'install'], pkg_dir)
            break

def installBowerPkgs(name, data, bower_pkgs):
    materials_dir = getDirMaterials(data, name)

    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    pkgs_info = data[R_MATERIALS_PKGS_DEP]
    for pkg_info in pkgs_info:
        if pkg_info['name'] == name :
            if 'bower' in pkg_info :
                print "bower exist!"
            else:
                pkg_info['bower'] = []

            for bower_pkg in bower_pkgs:
                pkg_info['bower'].append({'name':str(bower_pkg), 'version':str(bower_pkgs[bower_pkg])})

            #pprint.pprint(pkg_info)
            Template.parseAndSaveTemplate(materials_dir, name + os.sep + 'bower.json', pkg_dir, 'bower.json', pkg_info)
            Template.parseAndSaveTemplate(materials_dir, name + os.sep + 'bowerrc', pkg_dir, '.bowerrc', pkg_info)
            if os.name == "nt":
                proc=subprocess.Popen(['bower', 'install'], cwd=pkg_dir, shell=True)
            else:
                proc=subprocess.Popen(['bower', 'install'], cwd=pkg_dir)
            proc.wait()
            break

def installAppHtml(name, data, pkg_html_path, app_html_path):
    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    app_dir = getDirPrjApp(data, name)
    app_html_dir = getDirPrjAppHtml(data, name)
    app_js_dir = getDirPrjAppJs(data, name)
    app_css_dir = getDirPrjAppCss(data, name)
    app_images_dir = getDirPrjAppImages(data, name)

    Template.copyFile2File(pkg_html_dir, pkg_html_path, app_html_dir, app_html_path)

def installAppJs(name, data, pkg_js_path, app_js_path):
    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    app_dir = getDirPrjApp(data, name)
    app_html_dir = getDirPrjAppHtml(data, name)
    app_js_dir = getDirPrjAppJs(data, name)
    app_css_dir = getDirPrjAppCss(data, name)
    app_images_dir = getDirPrjAppImages(data, name)

    pkgs_info = data[R_MATERIALS_PKGS_DEP]
    for pkg_info in pkgs_info:
        if pkg_info['name'] == name :
            if 'js_seq' in pkg_info :
                print "js_seq exist"
            else:
                pkg_info['js_seq'] = []

            pkg_info['js_seq'].append(app_js_path)

            break

    Template.copyFile2File(pkg_js_dir, pkg_js_path, app_js_dir, app_js_path)

def installAppCss(name, data, pkg_css_path, app_css_path):
    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    app_dir = getDirPrjApp(data, name)
    app_html_dir = getDirPrjAppHtml(data, name)
    app_js_dir = getDirPrjAppJs(data, name)
    app_css_dir = getDirPrjAppCss(data, name)
    app_images_dir = getDirPrjAppImages(data, name)

    Template.copyFile2File(pkg_css_dir, pkg_css_path, app_css_dir, app_css_path)

def installAppImage(name, data, pkg_image_path, app_image_path):
    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    app_dir = getDirPrjApp(data, name)
    app_html_dir = getDirPrjAppHtml(data, name)
    app_js_dir = getDirPrjAppJs(data, name)
    app_css_dir = getDirPrjAppCss(data, name)
    app_images_dir = getDirPrjAppImages(data, name)

    Template.copyFile2File(pkg_image_dir, pkg_image_path, app_images_dir, app_image_path)

def installPkgHtml(name, data, src_html_path, pkg_html_path):
    materials_dir = getDirMaterials(data, name)

    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    Template.parseAndSaveTemplate(materials_dir, name + os.sep + src_html_path, pkg_html_dir, pkg_html_path, data)

def installPkgJs(name, data, src_js_path, pkg_js_path):
    materials_dir = getDirMaterials(data, name)

    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    Template.parseAndSaveTemplate(materials_dir, name + os.sep + src_js_path, pkg_js_dir, pkg_js_path, data)

def installPkgCss(name, data, src_css_path, pkg_css_path):
    materials_dir = getDirMaterials(data, name)

    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    Template.parseAndSaveTemplate(materials_dir, name + os.sep + src_css_path, pkg_css_dir, pkg_css_path, data)

def installPkgImage(name, data, src_image_path, pkg_image_path):
    materials_dir = getDirMaterials(data, name)

    material_dir = getDirMaterial(data, name)
    material_html_dir = getDirMaterialHtml(data, name)
    material_js_dir = getDirMaterialJs(data, name)
    material_css_dir = getDirMaterialCss(data, name)
    material_image_dir = getDirMaterialImage(data, name)

    pkg_dir = getDirPrjPkg(data, name)
    pkg_html_dir = getDirPrjPkgHtml(data, name)
    pkg_js_dir = getDirPrjPkgJs(data, name)
    pkg_css_dir = getDirPrjPkgCss(data, name)
    pkg_image_dir = getDirPrjPkgImage(data, name)

    Template.copyFile2File(material_image_dir, src_image_path , pkg_image_dir, pkg_image_path)

