class xlmodule(object):
    def __init__(self):
        self.numOrder = numOrder
        self.activityID = activityID
        self.sectionID = sectionID
        self.location = location
        self.modulename = modulename
        self.name = name
        self.intro = intro
        self.url = url
        self.grade = grade
        self.dueDate = dueDate
        self.content = content



class xlcourse(object):
    def __init__(self):
        self.location = location
        self.fullName = fullName
        self.shortName = shortName
        self.startDate = startDate



class xlsection(object):
    def __init__(self):
        self.number = number
        self.location = location
        self.name = name
        self.summary = summary
        self.activities = activities
        self.activities = list(filter(None, self.activities))
