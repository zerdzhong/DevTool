# -*- coding: utf-8 -*-

import os,sys,re,commands

LOAD_COUNT = 0

def findLoadInFramework(framworkPath, frameworkFile):

    nmPath = framworkPath + "/nm"
    cmd = "nm " + frameworkFile + " >" + nmPath
    os.system(cmd)
    loadCount = commands.getoutput("grep -Eo '.+\+\[.+ load\]$' " + nmPath + "| wc -l")
    if int(loadCount) > 0:
        print nmPath + " load Count:\t" + str(loadCount)

    return int(loadCount)

def findFramework(path):
    arr = path.split('/')
    if arr[-1].startswith('.'):
        return

    if not os.path.isdir(path):
        return

    global LOAD_COUNT
    folderList = os.listdir(path)
    for obj in folderList:
        if ".framework" in obj :
            frameworkPath = path + "/" + obj
            framworkFile = frameworkPath + "/" + obj.split('.')[0]
            if os.path.isfile(framworkFile):
                LOAD_COUNT += findLoadInFramework(frameworkPath, framworkFile)
        else:
            findFramework(path+"/"+obj)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "invalid path"
    else:

        findFramework(sys.argv[1])
        print "all loadCount: " + str(LOAD_COUNT)
