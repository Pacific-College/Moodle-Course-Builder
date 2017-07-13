from xml.sax.saxutils import escape, quoteattr

def xmlescape(data):
    return escape(data, entities={
        "'": "&apos;",
        "\"": "&quot;"
    })
