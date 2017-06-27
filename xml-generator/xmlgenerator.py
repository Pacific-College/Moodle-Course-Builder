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
from objxls import *
import xlxsparse

def main():
    sectionList, activityList, directory = readmainXML()

    #Initialize Module and Section Objects
    global objModule
    global objSection

    objModule = []
    objSection = []

    for x in range(0, len(sectionList)):
        objSection.append(section(sectionList[x][0], sectionList[x][1], sectionList[x][2], sectionList[x][3], sectionList[x][4]))
        print "\n\n-------------"
        print "Section " + objSection[x].number
        print "----------"
        print "Section Name: " + objSection[x].name
        print "Section Summary"
        print "-------------------"
        print objSection[x].summary
        print "\nActivity Index"
        print "--------------------"

        y = 0

        for activity in objSection[x].activities:
            # print activity
            for i in range(0, len(activityList)):
                if activityList[i][0] == activity:
                    # print activityList[i] #.index(activity)
                    activityID = activityList[i][0]
                    sectionID = activityList[i][1]
                    modulename = activityList[i][2]
                    location = activityList[i][4]
                    objModule.append(module(i, activityID, sectionID, location, modulename))
    print "Test activity 2: " + objModule[2].name

    print "Object Course: " + objCourse.fullName
    xlxsparse()
    return 1


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
    sectionName = getTextByTag(domSection, "name")
    sectionSummary = getTextByTag(domSection, "summary")
    activitySequence = getTextByTag(domSection, "sequence")

    """
    print "Section #: " + sectionNumber
    print "Section Summary: " + sectionSummary
    print "Sequence of Activities: " + activitySequence
    """

    return [sectionNumber, sectionPath, sectionName, sectionSummary, activitySequence]



def writeXML(tree, location):
    tree.write(datafile)
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

    global objCourse
    objCourse = course(domSource, fullPath)
    print "Course Name: " + objCourse.fullName


    def grabObjects(dom):
        # This function grabs <contents> -> <activities> from moodle_backup.xml

        # Initialize Arrays
        moduleids = domSource.getElementsByTagName("moduleid")
        moduleid = []
        sectionid = []
        modulename = []
        title = []
        location = []
        activityList = []
        section = []
        sectionList = []

        for i in range(0, len(moduleids)):
            sectionid.append(dom.getElementsByTagName("sectionid")[i])
            moduleid.append(dom.getElementsByTagName("moduleid")[i])
            modulename.append(dom.getElementsByTagName("modulename")[i])
            title.append(dom.getElementsByTagName("title")[i])
            location.append(dom.getElementsByTagName("directory")[i])

            section.append(int(getText(sectionid[i].childNodes)))
            activityList.append(showNode(i, moduleid[i], sectionid[i], modulename[i], title[i], location[i]))

        # section = set(section)
        sectionPath = os.path.join(directory, 'sections')
        # print "\nSections: "
        sectionPaths = os.listdir(sectionPath)

        if platform == "darwin":
            sectionPaths.remove('.DS_Store')
        # print sectionPaths

        for x in sectionPaths:
            sectionList.append(sectionParse(x, directory))
            # print x
            """
            Each sectionList contains (sectionNumber, sectionName, sectionSummary, and activitySequence) x number of sections
            """

        # sectionList.sort()
        sectionList = sorted(sectionList,key=lambda x:int(x[0]))

        # sorted(sectionList,key=operator.itemgetter(0))
        # print "\nActivities are located in the following sections: "
        # section = list(set(section))
        # section.sort()
        # print section

        print "\nSections Data"
        print "-------------"
        print "Number of Sections"
        print "(Including General Course Information)"
        print "--------------------------------------"
        print len(sectionList)

        return sectionList, activityList, directory


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
