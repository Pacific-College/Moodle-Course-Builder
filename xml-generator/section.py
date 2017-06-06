def section(location):
  domSource = parse(location)

  section = domSource.getElementsByTagName("section")
  sectionId = section.getAttribute('id')
  sectionNumber = domSource.getElementsByTagName("number")
  sectionNumber.childNodes
