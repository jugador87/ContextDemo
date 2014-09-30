import xml.etree.ElementTree as ET

class XCMLParser:
    # This class parses input XCML and constructs a hashmap representation of the content

    # Contains the root of the parsed tree
    root = []

    
    def parseXCMLString(self, xcmlString):
        self.root = ET.fromstring(xcmlString)

    def parseXCMLFile(self, xcmlFile):
        self.root = ET.parse(xcmlFile).getroot()

    def __init__(self, xcmlValue):
        try:
            self.parseXCMLFile(xcmlValue)
        except IOError as e:
            try:
                self.parseXCMLString(xcmlValue)
            except:
                raise IOError("Malformed filename or value for data:\n"
                              + xcmlValue)
