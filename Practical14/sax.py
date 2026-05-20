from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from datetime import datetime


class GOHandler(ContentHandler):
    def __init__(self):
        self.current = ""
        self.name = ""
        self.namespace = ""
        self.is_a_count = 0
        self.results = {
            "molecular_function": ("",0),
            "biological_process": ("",0),
            "cellular_component": ("",0)
        }

# notice: three functions should be included in the class
    # starting element
    def startElement(self, name, attrs):
        self.current = name # set current tag
        if name == "term": #遇到新term的时候重置
            self.name = ""
            self.namespace = ""
            self.is_a_count = 0

    # read characters
    def characters(self, content):
        if self.current == "name":
            self.name += content
        elif self.current == "namespace":
            self.namespace += content

    # ending element
    def endElement(self, name):
        if name == "is_a":
            self.is_a_count += 1

        elif name == "term": #说明一个Go term已经读取完毕
            if self.namespace in self.results:
                current_max = self.results[self.namespace][1]
                if self.is_a_count > current_max:
                    self.results[self.namespace] = (
                        self.name.strip(),
                        self.is_a_count
                    ) # store term，is_a_count
        self.current = ""


# run SAX parser
#calculate execution time
start_time = datetime.now()

parser = make_parser() # create parser
handler = GOHandler()# create handler
parser.setContentHandler(handler) # set handler
parser.parse("go_obo.xml")# parse XML file

end_time = datetime.now()
execution_time = end_time - start_time

# print results
for ontology in handler.results:
    term_name = handler.results[ontology][0]
    count = handler.results[ontology][1]

    print("Ontology:", ontology)
    print("GO term with most <is_a> elements:", term_name)
    print("Number of <is_a> elements:", count)
    print()

print("SAX execution time:", execution_time)

# comparison:
# SAX was the quickest parser in this test.