import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
# https://docs.python.org/2/library/xml.etree.elementtree.html
# https://docs.python.org/3/library/xml.etree.elementtree.html
from xml.dom.minidom import parse, parseString
# https://docs.python.org/3/library/xml.dom.minidom.html
import datetime
import operator

def main():
    sectionList, activityList = readmainXML()

    print "\nActivity List"
    print activityList

    for x in range(0, len(sectionList)):
        print "\nSection " + sectionList[x][0]
        print "----------"
        print "Section Description"
        print "-------------------"
        print sectionList[x][1]
        print "\nActivity Index"
        print "--------------------"
        activities = sectionList[x][2].split(',')
        for activity in activities:
            print activity
            try:
                print activityList.index(activity)
            except Exception as e:
                print "None"
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
    domSection = parse(sectionPath)
    print "Section Path: " + sectionPath
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

def assignParse(assignPath, directory):
    directory = os.path.join(directory, 'activities')
    assignPath = os.path.join(directory, assignPath)
    assignPath = os.path.join(assignPath, 'assign.xml')
    domAssign = parse(assignPath)
    print "Assignment Path: " + assignPath
    dueDate = getText(domSection.getElementsByTagName("duedate")[0].childNodes)
    dueDate = datetime.datetime.fromtimestamp(dueDate).strftime('%Y-%m-%dT%H:%M:%S')
    print "Date: " + str(dueDate)
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
    print "Object: " + str(tree)

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
        print "\nSections: "
        sectionPaths = os.listdir(sectionPath)
        sectionPaths.remove('.DS_Store')
        print sectionPaths

        for x in sectionPaths:
            sectionList.append(sectionParse(x, directory))
            # print x
            """
            Each sectionList contains (sectionNumber, sectionSummary, and activitySequence) x number of sections
            """

        # sectionList.sort()
        sectionList = sorted(sectionList,key=lambda x:int(x[0]))

        # sorted(sectionList,key=operator.itemgetter(0))
        print "\nActivities are located in the following sections: "
        section = list(set(section))
        section.sort()
        print section

        print "\nSections Data"
        print "-------------"
        print "Number of Sections"
        print "(Including General Course Information)"
        print "--------------------------------------"
        print len(sectionList)
        for x in range(0, len(sectionList)):
            print "\nSection " + sectionList[x][0]
            print "----------"
            print "Section Description"
            print "-------------------"
            print sectionList[x][1]
            print "\nActivities by number"
            print "--------------------"
            print sectionList[x][2]
        return sectionList, activityList

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

        print "\nIndex: " + str(index)
        print "Title: " + titleStr
        print "Module ID: " + moduleidStr
        print "Section ID: " + sectionidStr
        print "Module: " + modulenameStr
        print "Location: " + locationStr

        modLocation = os.path.join(directory, locationStr)
        modLocation = os.path.join(modLocation, modulenameStr.split('_')[0] + ".xml")
        print "Full Path: " + modLocation

        return [moduleidStr, sectionidStr, modulenameStr, titleStr, modLocation]
        # return 1 # getText(sectionid.childNodes)

    return grabObjects(domSource)

def writeXML():
    """
    USE FOR CREATING FILE:
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
    return 1

main()
