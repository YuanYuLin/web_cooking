#!/usr/bin/pyton2.7
import os
import libcook

def MAIN_DEPPKG(name, data):
    return {'any':['ngRoute', 'appConfig', 'menuLeftPhoto', 'menuTopItems']}

def MAIN(name, data, input_dir, output_dir):
    libcook.installPkgHtml(name, data, 'index.html', 'index.html')
    libcook.installPkgCss(name, data, 'app.css', 'app.css')
    libcook.installPkgCss(name, data, 'styles.css', 'styles.css')
    libcook.installPkgImage(name, data, 'android-desktop.png', 'android-desktop.png')
    libcook.installPkgImage(name, data, 'dog.png', 'dog.png')
    libcook.installPkgImage(name, data, 'favicon.png', 'favicon.png')
    libcook.installPkgImage(name, data, 'ios-desktop.png', 'ios-desktop.png')
    libcook.installPkgImage(name, data, 'user.jpg', 'user.jpg')

def MAIN_INSTALL(name, data):
    libcook.installAppHtml(name, data, 'index.html', 'index.html')
    libcook.installAppCss(name, data, 'app.css', 'app.css')
    libcook.installAppCss(name, data, 'styles.css', 'styles.css')

    libcook.installAppImage(name, data, 'android-desktop.png', 'android-desktop.png')
    libcook.installAppImage(name, data, 'dog.png', 'dog.png')
    libcook.installAppImage(name, data, 'favicon.png', 'favicon.png')
    libcook.installAppImage(name, data, 'ios-desktop.png', 'ios-desktop.png')
    libcook.installAppImage(name, data, 'user.jpg', 'user.jpg')

