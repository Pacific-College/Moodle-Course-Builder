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
from changetag import *
from escape import xmlescape
reload(sys)
sys.setdefaultencoding('utf-8')

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

def writeCourse(singleobjxl):
    print "Course Location: " + singleobjxl.location

    domSource = parse(singleobjxl.location)
    domSource.getElementsByTagName("original_course_fullname")[0].firstChild.nodeValue = singleobjxl.fullName
    domSource.getElementsByTagName("original_course_shortname")[0].firstChild.nodeValue = singleobjxl.shortName
    domSource.getElementsByTagName("original_course_startdate")[0].firstChild.nodeValue = unixTime(singleobjxl.startDate, '%Y-%m-%d')

    writeFile(domSource, singleobjxl.location)

def writeSection(singleobjxl):
    domSource = parse(singleobjxl.location)
    """
    print "Section Location: " + singleobjxl.location
    try:
        print "Section Name: " + singleobjxl.name
    except:
        print "Section Name: None"
    """
    try:
        domSource.getElementsByTagName("number")[0].firstChild.nodeValue = singleobjxl.number
    except:
        print "NONE"

    try:
        domSource.getElementsByTagName("name")[0].firstChild.nodeValue = singleobjxl.name
    except:
        print "NONE"

    try:
        domSource.getElementsByTagName("summary")[0].firstChild.nodeValue = singleobjxl.summary
    except:
        print "NONE"

    try:
        domSource.getElementsByTagName("sequence")[0].firstChild.nodeValue = singleobjxl.sequence
    except:
        print "NONE"

    writeFile(domSource, singleobjxl.location)

def writeActivity(singleobjxl):

    try:
        print "Activity Location: " + singleobjxl.location
    except:
        print "Activity Location: None"
    try:
        print "Activity Name: " + xmlescape(singleobjxl.name)
    except:
        print "Activity Name: None"


    domSource = parse(singleobjxl.location)

    try:
        domSource.getElementsByTagName("name")[0].firstChild.nodeValue = singleobjxl.name
    except:
        print "Empty Title Name"

    try:
        domSource.getElementsByTagName("intro")[0].firstChild.nodeValue = singleobjxl.intro
    except:
        print "Empty Intro"

    try:
        domSource.getElementsByTagName("content")[0].firstChild.nodeValue = singleobjxl.content
    except:
        print "Empty Content"

    try:
        domSource.getElementsByTagName("modulename")[0].firstChild.nodeValue = singleobjxl.modulename
    except:
        print "Empty Module Name"

    try:
        domSource.getElementsByTagName("url")[0].firstChild.nodeValue = singleobjxl.url
    except:
        print "Empty URL"

    try:
        domSource.getElementsByTagName("grade")[0].firstChild.nodeValue = singleobjxl.grade
    except:
        print "Empty Grade Value"

    try:
        domSource.getElementsByTagName("duedate")[0].firstChild.nodeValue = singleobjxl.dueDate
    except:
        print "Empty Due Date"

    changeID(singleobjxl.activityID, singleobjxl.moduleID, singleobjxl.location)
    changeSection(singleobjxl.sectionNumber, singleobjxl.moduleID, singleobjxl.sectionID, singleobjxl.modulePath)

    writeFile(domSource, singleobjxl.location)
