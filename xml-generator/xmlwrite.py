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
from objxls import *

def writeXML(objxlCourse, objxlSection, objxlModule):
    newText = "http://replacementurltest.com"


    writeCourse(objxlCourse)
    writeSection(objxlSection)
    writeModule(objxModule)

    modulexml = os.path.join(directory, 'module.xml')


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

def writeCourse(objxModule):
    domSource = parse(objxModule.location)
    domSource.getElementsByTageName("original_course_fullname")[0].firstChild.nodeValue = objxModule.fullName
    domSource.getElementsByTageName("original_course_shortname")[0].firstChild.nodeValue = objxModule.shortName
    domSource.getElementsByTageName("original_course_startdate")[0].firstChild.nodeValue = unixTime(objxModule.startDate)

def writeSection(singleobjxlSection):
    domSource = parse(singleobjxlSection.location)
    domSource.getElementsByTageName("sequence")[0].firstChild.nodeValue = singleobjxlSection.activities
