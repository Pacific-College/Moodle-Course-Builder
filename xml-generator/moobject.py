import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://docs.python.org/3/library/xml.etree.elementtree.html
from xml.dom.minidom import parse, parseString
# https://docs.python.org/3/library/xml.dom.minidom.html
from sys import platform
import time
import datetime
import operator

global objModule
global objSection
global objCourse

class module(object):
    name = ""
    intro = ""
    url = ""
    grade = ""
    dueDate = ""

    def __init__(self, activityID, location, modulename):
        self.activityID = activityID
        self.location = location
        self.modulename = modulename

        def assignParse(self):

            domActivity = parse(self.location)

            print("\n-------------")
            print("Module: " + self.modulename)
            print("Path: " + self.location)

            self.name = getTextByTag(domActivity, "name")
            print("Name: " + self.name)

            self.intro = getTextByTag(domActivity, "intro")
            print("Intro: " + self.intro)

            self.url = getTextByTag(domActivity, "externalurl")
            print("URL: " + self.url)

            self.grade = getTextByTag(domActivity, "grade")
            print("Assignment Grade: " + self.grade)

            # Format Due Date
            self.dueDate = getTextByTag(domActivity, "duedate")
            print("Unix Due Date: " + self.dueDate)

            dueDate = formatTime(self.dueDate)
            print("Formatted Due Date: " + dueDate)

            # modulePath = activityPath.replace('assign.xml','module.xml')
            # sectionId, sectionNumber, visible = parseModule(modulePath)
            # add sectionId and sectionNumber to Object
            return 1

        assignParse(self)



class course(object):
    def __init__(self, domCourse, location):
        self.domCourse = domCourse
        self.location = location
        self.fullName = getTextByTag(self.domCourse, "original_course_fullname")
        self.shortName = getTextByTag(self.domCourse, "original_course_shortname")
        self.startDate = getTextByTag(self.domCourse, "original_course_startdate")

        # For future, moving modules
        # self.moduleids = getText(self.domCourse.getElementsByTagName(moduleid)[0].childNodes)



class section(object):
    def __init__(self, number, location, name, summary, activities):
        self.number = number
        self.location = location
        self.name = name
        self.summary = summary
        self.activities = activities.split(',')



def formatTime(thisTime):
    #Convert Unix Timestamp into Readable Date
    try:
        return datetime.datetime.fromtimestamp(int(thisTime)).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return ""

def unixTime(thisTime):
    #Convert time string back into Unix Timestamp
    thisTime.mktime(datetime.datetime.strptime(datetime, '%Y-%m-%d %H:%M:%S').timetuple())
    return 1

def getTextByTag(dom, tagname):
    try:
        nodelist = dom.getElementsByTagName(tagname)[0].childNodes
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)
    except:
        pass
        return ""

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)
