from openpyxl import Workbook
from openpyxl import load_workbook

global objModule
global objSection
global objCourse

def main(objCourse, objSection, objModule):
    option = 0
    print "1. Import Excel File of Modification to a Moodle Backup at %s" % (objCourse.location)
    print "2. Write Excel File from Moodle Backup at %s" % (objCourse.location)
    try:
        option = raw_input("(1 or 2)")
    except:
        option = input("(1 or 2)")
    if choose(option, location) == 0:
        print "Invalid Option - Aborting."

    return 1



def choose(option):
    if option == "1":
        readXL()
    elif option == "2":
        writeXL()
    else:
        print "Invalid Option"
        return 0
    return 1



def readXL():
    try:
        directory = raw_input("Please enter the full path of the XLSX document \n (e.g. /Users/milesexner/Desktop/Moodle-Course/ws800-01.xlsx) : ")
    except:
        directory = input("Please enter the full path of the XLSX document \n (e.g. /Users/milesexner/Desktop/Moodle-Course/ws800-01.xlsx) : ")

    # fullPath = os.path.join(directory, filename)
    fullPath = directory

    try:
        print "Path: " + fullPath
        wb = load_workbook(filename = fullPath)
    except:
        print "Sorry, could not open %s. Please try again." % (fullPath)
        return 0



def writeXL():
    wb = Workbook()
    destFilename = course.shortName + ".xlsx"
    print "File will be written as " + filename
    courseSheet(wb)
    wb.save(filename = destFilename)



def courseSheet():
    wsCourse = wb.active

    wsCourse['A1'] = "Short Name"
    wsCourse['A2'] = "Full Name"
    wsCourse['A3'] = "Start Date"
    wsCourse['A4'] = "Backup Location"

    wsCourse['B1'] = xmlgenerator.objCourse.shortName
    wsCourse['B2'] = xmlgenerator.objCourse.fullName
    wsCourse['B3'] = xmlgenerator.objCourse.startDate
    wsCourse['B4'] = xmlgenerator.objCourse.location
    writeSheet("Course", 0)
    return 1



def writeSheet(name, numSheet):
    ws = wb.create_sheet(name, numSheet)
    return 1



def readSheets():
    print wb.get_sheet_names()
    return 1
