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
from .objxls import *
from .xlxsparse import *
import sys
import imp
imp.reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    """
    Returns sectionList, which contains the Section Number, Path, Name, Summary, and Sequence of Activities by ID
    Returns activityList, which contains the activity ID, section ID that the activity belongs to, the name of the module, and the location of the module file
    Returns directory, which is the root directory of the extracted Moodle Backup, and isn't being used
    """

    sectionList, activityList, directory = readmainXML()

    #Initialize Module and Section Objects
    global objModule
    global objSection

    objModule = []
    objSection = []

    """
    Here we build the Section and Activity/Module Objects with classes defined in objxls.py
    The course object, which contains basic course data such as the location of the moodle_backup.xml file,
    short name, long name, and course start date. That is built right away when the moodle_backup.xml file is first read.
    """
    for x in range(0, len(sectionList)):
        objSection.append(section(sectionList[x][0], sectionList[x][1], sectionList[x][2], sectionList[x][3], sectionList[x][4]))
        """
        Tests
        print "\n\n-------------"
        print "Section " + objSection[x].number
        print "----------"
        print "Section Name: " + objSection[x].name
        print "Section Summary"
        print "-------------------"
        print objSection[x].summary
        print "\nActivity Index"
        print "--------------------"
        """
        y = 0

        for activity in objSection[x].activities:
            # print activity
            for i in range(0, len(activityList)):
                if activityList[i][0] == activity:
                    # print activityList[i] #.index(activity)
                    moduleID = activityList[i][0]
                    sectionID = activityList[i][1]
                    modulename = activityList[i][2]
                    location = activityList[i][4]
                    objModule.append(module(i, moduleID, sectionID, location, modulename))
    # print "Test activity 2: " + objModule[2].name

    # print "Object Course: " + objCourse.fullName
    xlxsparse(objCourse, objSection, objModule)
    return 1

"""
Grabs the data from a section.xml file and returns it to the sectionList (in the grabObjects function), which gets appended to the objSection class object.
"""
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


"""
readmainXML parses the moodle_backup.xml after prompting the user for the location
"""
def readmainXML():

    try:
        directory = input("Please enter the full path of moodle_backup.xml \n (e.g. /Users/milesexner/Desktop/Moodle-Course/ws800-01) : ")
    except:
        directory = eval(input("Please enter the full path of moodle_backup.xml \n (e.g. /Users/milesexner/Desktop/Moodle-Course/ws800-01) : "))

    # If left blank use testing default
    if directory == "":
        directory = "/Users/milesexner/Desktop/Moodle-Course/ws800-01"

    fullPath = os.path.join(directory, 'moodle_backup.xml')

    try:
        print("Path: " + fullPath)
        tree = ET.parse(fullPath) # parse as an XML ElementTree
        domSource = parse(fullPath) # parse as a DOM
    except:
        print("Sorry, could not parse moodle_backup.xml. Please try again.")

    print("Parsing XML Files...")

    # print "Object: " + str(tree)

    """
    Courses are built automatically by the course class in objxls.py
    """
    global objCourse
    objCourse = course(domSource, fullPath)
    print("Course Name: " + objCourse.fullName)


    def grabObjects(dom):
        """
        This function grabs <contents> -> <activities> from moodle_backup.xml
        This is the data that points to where the other data is located
        """
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

        """
        This runs through all of the activities/modules in the moodle_backup.xml file and creates the activities and section lists
        """
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

        """
        On MacOS, we need to remove .DS_Store
        """
        if platform == "darwin":
            try:
                sectionPaths.remove('.DS_Store')
                print(".DS_Store File Found and Removed from List")
            except:
                print(".DS_Store File Not Found")
        # print sectionPaths

        """
        We loop through the directory of sections to grab all of the section data from the section.xml files
        with the sectionParse function and sort the list in order of the section number
        """
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

        """
        Tests
        print "\nSections Data"
        print "-------------"
        print "Number of Sections"
        print "(Including General Course Information)"
        print "--------------------------------------"
        print len(sectionList)
        """
        return sectionList, activityList, directory

    """
    showNode uses the getText function to get the text from the nodes for activities
    Most importantly, this finds the location of the activity/module xml file
    """
    def showNode(index, moduleid, sectionid, modulename, title, location):
        titleStr = getText(title.childNodes)
        moduleidStr = getText(moduleid.childNodes)
        sectionidStr = getText(sectionid.childNodes)
        modulenameStr = getText(modulename.childNodes)
        locationStr = getText(location.childNodes)

        """ Tests
        print "\nIndex: " + str(index)
        print "Title: " + titleStr
        print "Module ID: " + moduleidStr
        print "Section ID: " + sectionidStr
        print "Module: " + modulenameStr
        print "Location: " + locationStr
        """

        """
        Build the location of the activity/module xml file
        """
        modLocation = os.path.join(directory, locationStr)
        modLocation = os.path.join(modLocation, modulenameStr.split('_')[0] + ".xml")
        # print "Full Path: " + modLocation

        return [moduleidStr, sectionidStr, modulenameStr, titleStr, modLocation]
        # return 1 # getText(sectionid.childNodes)

    return grabObjects(domSource)

main()
