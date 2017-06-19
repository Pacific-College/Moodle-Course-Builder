import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://docs.python.org/3/library/xml.etree.elementtree.html
from xml.dom.minidom import parse, parseString
# https://docs.python.org/3/library/xml.dom.minidom.html
import time
import datetime
import operator

def readmainXML():
    newText = "http://replacementurltest.com"
    try:
        directory = raw_input("Please enter the full path of test.xml \n (e.g. /Users/milesexner/Desktop/Moodle-Course/xml-generator/Test) : ")
    except:
        directory = input("Please enter the full path of test.xml \n (e.g. /Users/milesexner/Desktop/Moodle-Course/xml-generator/Test) : ")

    fullPath = os.path.join(directory, 'test.xml')

    try:
        print "Path: " + fullPath
        tree = ET.parse(fullPath) # parse as an XML ElementTree
        domSource = parse(fullPath) # parse as a DOM
    except:
        print "Sorry, could not parse test.xml. Please try again."
        return 0
    print "URL Name: " + getText(domSource.getElementsByTagName("name")[0].childNodes)
    print "URL: " + getText(domSource.getElementsByTagName("externalurl")[0].childNodes)

    domSource.getElementsByTagName("externalurl")[0].firstChild.nodeValue = newText

    print "URL: " + getText(domSource.getElementsByTagName("externalurl")[0].childNodes)
    newFile = open('testres.xml', "w")
    domSource.writexml(newFile, encoding="utf-8")
    newFile.close()
    # modulePath = activityPath.replace('url.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
    # add sectionId and sectionNumber to Object
    return 1

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

readmainXML()
