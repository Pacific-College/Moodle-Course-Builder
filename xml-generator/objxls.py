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
from openpyxl import Workbook
from openpyxl import load_workbook
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
ALL Objects Contained in this file with time formatting and XML tag reading functions
"""

class xlmodule(object):
    def __init__(self, modulename, sectionNumber, sectionID, moduleID, activityID, location, modulePath, name, intro, content, url, grade, dueDate ):
        self.numOrder = ""
        self.sectionNumber = sectionNumber
        self.moduleID = moduleID
        self.sectionID = sectionID
        self.activityID = activityID
        self.location = location
        self.modulePath = modulePath
        self.modulename = modulename
        self.name = name
        self.intro = intro
        self.url = url
        self.grade = grade
        self.dueDate = dueDate
        self.content = content

class xlcourse(object):
    def __init__(self):
        self.location = ""
        self.fullName = ""
        self.shortName = ""
        self.startDate = ""



class xlsection(object):
    def __init__(self, number, name, summary, location, sequence):
        self.number = number
        self.location = location
        self.name = name
        self.summary = summary
        self.sequence = sequence
        self.activities = []


class module(object):
    name = ""
    intro = ""
    url = ""
    grade = ""
    dueDate = ""
    modulePath = ""

    def __init__(self, numOrder, moduleID, sectionID, location, modulename):
        self.numOrder = numOrder
        self.moduleID = moduleID
        self.sectionID = sectionID
        self.location = location
        self.modulename = modulename

        def assignParse(self):

            # Fills in the rest of the fields from the activity's xml file
            domActivity = parse(self.location)

            """
            print "\n-------------"
            print "Module: " + self.modulename
            print "Path: " + self.location
            """

            self.name = getTextByTag(domActivity, "name")
            # print "Name: " + self.name

            self.intro = getTextByTag(domActivity, "intro")
            # print "Intro: " + self.intro

            self.url = getTextByTag(domActivity, "externalurl")
            # print "URL: " + self.url

            self.grade = getTextByTag(domActivity, "grade")
            # print "Assignment Grade: " + self.grade

            # Format Due Date
            self.dueDate = getTextByTag(domActivity, "duedate")
            # print "Unix Due Date: " + self.dueDate

            self.content = getTextByTag(domActivity, "content")

            dueDate = formatTime(self.dueDate, '%Y-%m-%d %H:%M')
            # print "Formatted Due Date: " + dueDate

            self.modulePath = self.location.rsplit('/',1)[0] + "/module.xml"

            activity = domActivity.getElementsByTagName("activity")

            self.activityID = activity[0].getAttribute('id')


            domModule = parse(self.modulePath)
            self.sectionNumber = getTextByTag(domModule, "sectionnumber")

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

        # For future, implement moving modules
        # self.moduleids = getText(self.domCourse.getElementsByTagName(moduleid)[0].childNodes)



class section(object):
    def __init__(self, number, location, name, summary, activities):
        self.number = number
        self.location = location
        self.name = name
        self.summary = summary
        self.sequence = activities
        self.activities = activities.split(',')
        self.activities = list(filter(None, self.activities))


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


def formatTime(thisTime, timeFormat):
    # Convert Unix Timestamp into Readable Date
    try:
        return datetime.datetime.fromtimestamp(int(thisTime)).strftime(timeFormat)
    except:
        return ""

def unixTime(thisTime, timeFormat):
    # Convert time string back into Unix Timestamp
    try:
        return str(int(time.mktime(datetime.datetime.strptime(thisTime, timeFormat).timetuple())))
    except:
        return ""
