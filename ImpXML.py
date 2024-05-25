from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from ImpExp import ImpExp 

class ImpXML(ImpExp):
    def __init__(self, filename):
        super().__init__(filename)

    def RunOperation(self):
        try:
            tree = ET.parse(self.filename)
            root = tree.getroot()
            new_data = {}

            for elem in root:
                tag = elem.tag
                if tag not in new_data:
                    new_data[tag] = []
                new_data[tag].append(elem.attrib)

            self.FetchData(new_data)
            self.ImportSuccessful()
        except Exception as e:
            raise Exception(f"Error parsing XML: {str(e)}")