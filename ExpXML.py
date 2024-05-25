from abc import ABC, abstractmethod
from ImpExp import ImpExp
import xml.etree.ElementTree as ET

class ExpXML(ImpExp):
    def __init__(self, filename):
        super().__init__(filename)

    def RunOperation(self):
        try:
            root = ET.Element('data')
            self._dict_to_xml(self.data, root)
            tree = ET.ElementTree(root)
            with open(self.filename, 'wb') as file:
                tree.write(file, encoding='utf-8', xml_declaration=True)
            self.ImportSuccessful()
        except Exception as e:
            raise Exception(f"{Const.GET_ERROR('ERROR_EXPXML')} {str(e)}")

    def _dict_to_xml(self, data, parent):
        for key, value in data.items():
            if isinstance(value, dict):
                child = ET.SubElement(parent, key)
                self._dict_to_xml(value, child)
            elif isinstance(value, list):
                for item in value:
                    self._dict_to_xml({key: item}, parent)
            else:
                ET.SubElement(parent, key).text = str(value)