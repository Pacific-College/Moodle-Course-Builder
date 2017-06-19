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

class activity(object):
    def __init__(self, activityID, name, section, type, location):
        self.activityID = activityID
        self.name = name
        self.section = sectionList
        self.type = type
        self.location = location

class section(object):
    def __init__(self, sectionID, location, title, description, activityList):
        self.sectionID = sectionID
        self.location = location
        self.title = title
        self.description = Description
        self.activityList = activityList

def main():
    sectionList, activityList, directory = readmainXML()

    """
    Print for testing
    -----------------
    print "\nActivity List"
    print activityList
    """
    for x in range(0, len(sectionList)):
        print "\n\n-------------"
        print "Section " + sectionList[x][0]
        print "----------"
        print "Section Description"
        print "-------------------"
        print sectionList[x][1]
        print "\nActivity Index"
        print "--------------------"
        activities = sectionList[x][2].split(',')
        for activity in activities:
            # print activity
            for i in range(0, len(activityList)):
                try:
                    if activityList[i][0] == activity:
                        # print activityList[i] #.index(activity)
                        modulename = activityList[i][2]
                        location = activityList[i][4]

                        if modulename == "assign":
                            print "\nAssignment\n-----------"
                            assignParse(location)
                        elif modulename == "page":
                            print "\nPage Resource\n--------------"
                            pageParse(location)
                        elif modulename == "url":
                            print "\nURL\n-----------------"
                            urlParse(location)
                        elif modulename == "resource":
                            print "\nFile Resource\n------------------"
                            fileResourceParse(location)
                        elif modulename == "forum":
                            print "\nBasic Forum (e.g. Anouncments)\n------------"
                            forumParse(location)
                        elif modulename == "hsuforum":
                            print "\nAdvanced Forum\n-----------------"
                            hsuforumParse(location)
                        elif modulename == "questionnaire":
                            print "\nQuestionaire\n--------------------"
                            qaParse(location)
                        elif modulename == "folder":
                            print "\nFolder\n----------------"
                            folderParse(location)
                        elif modulename == "quiz":
                            print "\nQuiz\n--------------------"
                            quizParse(location)
                        else:
                            print "Module Not Implemented: " + activityList[i][0]
                            print "Report to mexner@pacificcollege.edu"


                except Exception as e:
                    # print None"
                    pass

def moveAct():
    return 0

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
    sectionNumber = getText(domSection.getElementsByTagName("number")[0].childNodes)
    sectionSummary = getText(domSection.getElementsByTagName("summary")[0].childNodes)
    activitySequence = getText(domSection.getElementsByTagName("sequence")[0].childNodes)

    """
    print "Section #: " + sectionNumber
    print "Section Summary: " + sectionSummary
    print "Sequence of Activities: " + activitySequence
    """

    return [sectionNumber, sectionSummary, activitySequence]

def assignParse(activityPath):
    """
    directory = os.path.join(directory, 'activities')
    activityPath = os.path.join(directory, activityPath)
    activityPath = os.path.join(activityPath, 'assign.xml')
    """
    domActivity = parse(activityPath)
    print "Assignment Path: " + activityPath
    print "Assignment Name: " + getText(domActivity.getElementsByTagName("name")[0].childNodes)
    print "Assignment Intro"
    print "----------------"
    print getText(domActivity.getElementsByTagName("intro")[0].childNodes)
    print "Assignment Grade: " + getText(domActivity.getElementsByTagName("grade")[0].childNodes)
    # Format Due Date
    dueDate = getText(domActivity.getElementsByTagName("duedate")[0].childNodes)
    print "Due Date: " + dueDate
    dueDate = datetime.datetime.fromtimestamp(int(dueDate)).strftime('%Y-%m-%d %H:%M:%S')
    print "Formatted Due Date: " + dueDate

    # modulePath = activityPath.replace('assign.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
    # add sectionId and sectionNumber to Object
    return 1

def urlParse(activityPath):
    domActivity = parse(activityPath)
    print "URL Path: " + activityPath
    print "URL Name: " + getText(domActivity.getElementsByTagName("name")[0].childNodes)
    print "URL: " + getText(domActivity.getElementsByTagName("externalurl")[0].childNodes)

    # modulePath = activityPath.replace('url.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
    # add sectionId and sectionNumber to Object
    return 1

def hsuforumParse(activityPath):
    domActivity = parse(activityPath)
    print "Forum Path: " + activityPath
    print "Forum Name: " + getText(domActivity.getElementsByTagName("name")[0].childNodes)
    print "Forum Intro"
    print "----------------"
    print getText(domActivity.getElementsByTagName("intro")[0].childNodes)
    print "Assignment Grade: " + getText(domActivity.getElementsByTagName("grade")[0].childNodes)

    # modulePath = activityPath.replace('hsuforum.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
    # add sectionId and sectionNumber to Object
    return 1

def forumParse(activityPath):
    domActivity = parse(activityPath)
    print "Forum Path: " + activityPath
    print "Forum Name: " + getText(domActivity.getElementsByTagName("name")[0].childNodes)
    print "Forum Intro"
    print "----------------"
    print getText(domActivity.getElementsByTagName("intro")[0].childNodes)

    # modulePath = activityPath.replace('forum.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
    # add sectionId and sectionNumber to Object
    return 1

def pageParse(activityPath):
    domActivity = parse(activityPath)
    print "Page Path: " + activityPath
    print "Page Name: " + getText(domActivity.getElementsByTagName("name")[0].childNodes)
    print "Page Intro"
    print "----------------"
    print getText(domActivity.getElementsByTagName("intro")[0].childNodes)
    print "Page Content"
    print "------------"
    print getText(domActivity.getElementsByTagName("content")[0].childNodes)

    # modulePath = activityPath.replace('page.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
    # add sectionId and sectionNumber to Object
    return 1

def fileResourceParse(activityPath):
    domActivity = parse(activityPath)
    print "File Path: " + activityPath
    print "File Title: " + getText(domActivity.getElementsByTagName("name")[0].childNodes)
    print
    # modulePath = activityPath.replace('page.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
    # add sectionId and sectionNumber to Object
    return 1

def folderParse(activityPath):
    domActivity = parse(activityPath)
    print "Folder Path: " + activityPath
    print "Folder Name: " + getText(domActivity.getElementsByTagName("name")[0].childNodes)
    print "Folder Intro"
    print "----------------"
    print getText(domActivity.getElementsByTagName("intro")[0].childNodes)

    # modulePath = activityPath.replace('page.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
    return 1

def qaParse(activityPath):
    domActivity = parse(activityPath)
    print "QA Path: " + activityPath
    print "QA Name: " + getText(domActivity.getElementsByTagName("name")[0].childNodes)

    # modulePath = activityPath.replace('page.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
    return 1

def quizParse(activityPath):
    domActivity = parse(activityPath)
    print "Quiz Path: " + activityPath
    print "Quiz Name: " + getText(domActivity.getElementsByTagName("name")[0].childNodes)
    print "Quiz Intro"
    print "----------------"
    print getText(domActivity.getElementsByTagName("intro")[0].childNodes)

    # modulePath = activityPath.replace('page.xml','module.xml')
    # sectionId, sectionNumber, visible = parseModule(modulePath)
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

def changeValue():
    return 1

def writeXML(tree, location):
    tree.write(datafile)
    return 1

def readDoc():
    #Convert time string back into Unix Timestamp
    time.mktime(datetime.datetime.strptime(datetime, "%d/%m/%Y").timetuple())
    return 1
main()
