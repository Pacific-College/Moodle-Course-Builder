from xml.sax.saxutils import escape, quoteattr

def main():
    pretty_xml = '<title>Kligler & Weeks "2014", <Langevin et al 2001> and MacPherson et al. 2016</title'


    pretty_xml = xmlescape(pretty_xml)
    print(pretty_xml)

def xmlescape(data):
    return escape(data, entities={
        "'": "&apos;",
        "\"": "&quot;"
    })

main()
