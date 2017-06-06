import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://docs.python.org/3/library/xml.etree.elementtree.html
from xml.dom.minidom import parse, parseString
# https://docs.python.org/3/library/xml.dom.minidom.html

def main():
    """
    USE FOR CREATING FILE:

    dirList = ['activities','course','files','local','sections']
    try:
        directory = raw_input("Please enter a path : ")
        name = raw_input("Please enter a  filename : ")
    except:
        directory = input("Please enter a path : ")
        name  = input("Please enter a filename : ")
    try:
        os.makedirs(directory)
    except:
        x = 1
    filename = directory+ "\ "+name+".xml"
    num = int(input("How many tags would you like in your xml file : "))
    a = open(filename,"w")
    a.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    for i in range(num):
       try:
           tag = raw_input("Please enter a tag name : ")
       except:
            tag = input("Please enter a tag name : ")
       tag_fix = "<"+tag+">"+" "+"</"+tag+">"+"\n"
       a.write(tag_fix)
    a.close()
    return 1
    """

def readXML():

    try:
        directory = raw_input("Please enter the full path of moodle_backup.xml \n (e.g. /Users/milesexner/Desktop/Moodle-Course/ws800-01) : ")
    except:
        directory = input("Please enter the full path of moodle_backup.xml \n (e.g. /Users/milesexner/Desktop/Moodle-Course/ws800-01) : ")

    fullPath = os.path.join(directory, 'moodle_backup.xml')

    try:
        print "Path: " + fullPath
        tree = ET.parse(fullPath) # parse as an XML ElementTree
        domSource = parse(fullPath) # parse as a DOM
    except:
        print "Sorry, could not parse moodle_backup.xml. Please try again."
        return 0
    print "Object: " + str(tree)

    def grabObjects(dom):
        activities = dom.getElementsByTagName("activity")
        sectionid = []
        modulename = []
        title = []
        directory = []
        for i in range(0, len(activities)):
            sectionid.append(dom.getElementsByTagName("sectionid")[i])
            modulename.append(dom.getElementsByTagName("modulename")[i])
            title.append(dom.getElementsByTagName("title")[i])
            directory.append(dom.getElementsByTagName("directory")[i])

            showNode(i, sectionid[i], modulename[i], title[i], directory[i])
        return 1

    """
    def printSections():
        activities = list(tree.iter("activity"))
        for i in activities:
            print tostring(i) #, encoding='UTF-8', method='xml')
    """
    # printSections()

    def getText(nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)

    def showNode(index, sectionid, modulename, title, directory):
        print ""
        print "Index: " + str(index)
        print "Title: " + getText(title.childNodes)
        print "Section ID: " + getText(sectionid.childNodes)
        print "Module: " + getText(modulename.childNodes)
        print "Location: " + getText(directory.childNodes)

        

    grabObjects(domSource)
    return 1

"""
sectionid
title
directory
"""


def writeXML():
    return 1

readXML()
