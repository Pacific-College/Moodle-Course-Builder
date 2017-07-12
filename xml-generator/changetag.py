import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom.minidom import parse, parseString
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def changeID(activityid, moduleid, sourceFile):
    domSource = parse(sourceFile)
    try:
        print "Change ID File: " + sourceFile
        print "Activity ID: " + activityid
        print "Module ID: " + moduleid
    except:
        print "NONE"

    activity = domSource.getElementsByTagName("activity")

    activity[0].setAttribute('id', activityid)
    activity[0].setAttribute('moduleid', moduleid)

    writeFile(domSource, sourceFile)

def changeSection(sectionNumber, moduleid, sectionid, sourceFile):
    domSource = parse(sourceFile)

    module = domSource.getElementsByTagName("module")

    module[0].setAttribute('id', moduleid)

    domSource.getElementsByTagName("sectionid")[0].firstChild.nodeValue = sectionid
    domSource.getElementsByTagName("sectionnumber")[0].firstChild.nodeValue = sectionNumber

    writeFile(domSource, sourceFile)


def writeFile(domSource, sourceFile):
    newFile = open(sourceFile, "w")
    domSource.writexml(newFile, encoding="utf-8")
    newFile.close()
