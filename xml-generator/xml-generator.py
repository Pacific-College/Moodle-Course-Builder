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

            print "\n-------------"
            print "Module: " + self.modulename
            print "Path: " + self.location
            
            self.name = getTextByTag(domActivity, "name")
            print "Name: " + self.name

            self.intro = getTextByTag(domActivity, "intro")
            print "Intro: " + self.intro

            self.url = getTextByTag(domActivity, "externalurl")
            print "URL: " + self.url

            self.grade = getTextByTag(domActivity, "grade")
            print "Assignment Grade: " + self.grade

            # Format Due Date
            self.dueDate = getTextByTag(domActivity, "duedate")
            print "Unix Due Date: " + self.dueDate

            dueDate = formatTime(self.dueDate)
            print "Formatted Due Date: " + dueDate

            # modulePath = activityPath.replace('assign.xml','module.xml')
            # sectionId, sectionNumber, visible = parseModule(modulePath)
            # add sectionId and sectionNumber to Object
            return 1

        assignParse(self)


class section(object):
    def __init__(self, sectionID, location, title, description, activityList):
        self.sectionID = sectionID
        self.location = location
        self.title = title
        self.description = Description
        self.activityList = activityList



def main():
    sectionList, activityList, directory = readmainXML()

    for x in range(0, len(sectionList)):
        print "\n\n-------------"
        print "Section " + sectionList[x][0]
        print "----------"
        print "Section Intro"
        print "-------------------"
        print sectionList[x][1]
        print "\nActivity Index"
        print "--------------------"
        activities = sectionList[x][2].split(',')
        objModule = []
        y = 0

        for activity in activities:
            # print activity
            for i in range(0, len(activityList)):
                if activityList[i][0] == activity:
                    # print activityList[i] #.index(activity)
                    modulename = activityList[i][2]
                    location = activityList[i][4]
                    objModule.append(module(i, location, modulename))
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

# Parse Section data
def sectionParse(sectionPath, directory):
    activitySequence = []
    directory = os.path.join(directory, 'sections')
    sectionPath = os.path.join(directory, sectionPath)
    sectionPath = os.path.join(sectionPath, 'section.xml')
    tree = ET.parse(sectionPath)
    domSection = parse(sectionPath)
    # print "Section Path: " + sectionPath
    # get Section number from section_382901.xml
    # sectionId = domSection.getElementsByTagName("section").getAttribute('id')
    sectionNumber = getTextByTag(domSection, "number")
    sectionSummary = getTextByTag(domSection, "summary")
    activitySequence = getTextByTag(domSection, "sequence")

    """
    print "Section #: " + sectionNumber
    print "Section Summary: " + sectionSummary
    print "Sequence of Activities: " + activitySequence
    """

    return [sectionNumber, sectionSummary, activitySequence]



def options():
    print "What would you like to do?"
    print "--------------------------"
    print "1. Edit Sections"
    print "2. Edit Activities"
    try:
        choice = raw_input()
    except:
        choice = input()
    try:
        if int(choice) < 1 and int(choice) > 2:
            print "Please pick 1 or 2"
            options()
    except:
        print "Please pick 1 or 2"
        options()
    if int(choice) == 1:
        editSection()
    else:
        editActivity()
    return 1


def writeXML(tree, location):
    tree.write(datafile)
    return 1

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



def readmainXML():
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
    # print "Object: " + str(tree)

    def grabObjects(dom):
        moduleid = dom.getElementsByTagName("moduleid")
        sectionid = []
        modulename = []
        title = []
        location = []
        activityList = []
        section = []
        sectionList = []
        for i in range(0, len(moduleid)):
            sectionid.append(dom.getElementsByTagName("sectionid")[i])
            moduleid.append(dom.getElementsByTagName("moduleid")[i])
            modulename.append(dom.getElementsByTagName("modulename")[i])
            title.append(dom.getElementsByTagName("title")[i])
            location.append(dom.getElementsByTagName("directory")[i])

            section.append(int(getText(sectionid[i].childNodes)))
            activityList.append(showNode(i, moduleid[i], sectionid[i], modulename[i], title[i], location[i]))

        # section = set(section)
        """
        SECTIONS
        """
        sectionPath = os.path.join(directory, 'sections')
        # print "\nSections: "
        sectionPaths = os.listdir(sectionPath)
        if platform == "Darwin":
            sectionPaths.remove('.DS_Store')
        # print sectionPaths

        for x in sectionPaths:
            sectionList.append(sectionParse(x, directory))
            # print x
            """
            Each sectionList contains (sectionNumber, sectionSummary, and activitySequence) x number of sections
            """

        # sectionList.sort()
        sectionList = sorted(sectionList,key=lambda x:int(x[0]))

        # sorted(sectionList,key=operator.itemgetter(0))
        # print "\nActivities are located in the following sections: "
        section = list(set(section))
        section.sort()
        # print section

        print "\nSections Data"
        print "-------------"
        print "Number of Sections"
        print "(Including General Course Information)"
        print "--------------------------------------"
        print len(sectionList)
        """
        Print for Debugging Purposes
        for x in range(0, len(sectionList)):
            print "\n\n----------------------"
            print "Section " + sectionList[x][0]
            print "----------"
            print "Section Description"
            print "-------------------"
            print sectionList[x][1]
            print "\nActivities by number"
            print "--------------------"
            print sectionList[x][2]
        """
        return sectionList, activityList, directory

    """
    def printSections():
        activities = list(tree.iter("activity"))
        for i in activities:
            print tostring(i) #, encoding='UTF-8', method='xml')
    """
    # printSections()

    def showNode(index, moduleid, sectionid, modulename, title, location):
        titleStr = getText(title.childNodes)
        moduleidStr = getText(moduleid.childNodes)
        sectionidStr = getText(sectionid.childNodes)
        modulenameStr = getText(modulename.childNodes)
        locationStr = getText(location.childNodes)
        """
        print "\nIndex: " + str(index)
        print "Title: " + titleStr
        print "Module ID: " + moduleidStr
        print "Section ID: " + sectionidStr
        print "Module: " + modulenameStr
        print "Location: " + locationStr
        """
        modLocation = os.path.join(directory, locationStr)
        modLocation = os.path.join(modLocation, modulenameStr.split('_')[0] + ".xml")
        # print "Full Path: " + modLocation

        return [moduleidStr, sectionidStr, modulenameStr, titleStr, modLocation]
        # return 1 # getText(sectionid.childNodes)

    return grabObjects(domSource)



main()
