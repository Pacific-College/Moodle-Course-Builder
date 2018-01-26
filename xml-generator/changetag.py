import os
from xml.dom.minidom import parse, parseString
import sys
import re
from xml.sax.saxutils import escape, quoteattr
import imp
imp.reload(sys)
sys.setdefaultencoding('utf-8')

def changeID(activityid, moduleid, sourceFile):
    domSource = parse(sourceFile)
    try:
        print("Change ID File: " + sourceFile)
        print("Activity ID: " + activityid)
        print("Module ID: " + moduleid)
    except:
        print("NONE")

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

def changeVisible(visible, sourceFile):
    domSource = parse(sourceFile)

    domSource.getElementsByTagName("visible")[0].firstChild.nodeValue = visible

    writeFile(domSource, sourceFile)

def writeFile(domSource, sourceFile):
    ugly_xml = domSource.toxml()
    ugly_xml = domSource.toprettyxml(indent="", newl='', encoding="UTF-8")

    text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
    pretty_xml = text_re.sub('>\g<1></', ugly_xml)

    with open(sourceFile, "w") as config_file:
        config_file.write(pretty_xml)
    # newFile = open(sourceFile, "w")
    # domSource.writexml(newFile, encoding="utf-8")
    config_file.close()
