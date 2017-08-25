#!/usr/bin/python2.7

import json

def _jsValue(obj, key):
    if key in obj:
        return obj[key]
        return None

def jsInt(obj, key):
    val = _jsValue(obj, key)
    if val == None:
        return 0
    return val

def jsString(obj, key):
    val = _jsValue(obj, key)
    if val == None:
        return ""
    return val

def jsArray(obj, key):
    val = _jsValue(obj, key)
    if val == None:
        return []
    return val

def createDataNode(data, name):
    data[name] = {}
    return data[name]

def createListNode(data, name):
    data[name] = []
    return data[name]

def loadJson2Obj(config):
    with open(config) as fd:
        data = json.load(fd)
    return data
