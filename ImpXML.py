from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
from ImpExp import ImpExp 
from Const import Const

class ImpXML(ImpExp):
    def __init__(self, filename):
        super().__init__(filename)

    def xml_to_dict(self, element):
        def _xml_to_dict_recursion(elem):
            children = list(elem)
            if not children:
                return elem.text
            result_dict = {}
            for child in children:
                child_result = _xml_to_dict_recursion(child)
                if child.tag in result_dict:
                    if isinstance(result_dict[child.tag], list):
                        result_dict[child.tag].append(child_result)
                    else:
                        result_dict[child.tag] = [result_dict[child.tag], child_result]
                else:
                    result_dict[child.tag] = child_result
            return result_dict

        return {element.tag: _xml_to_dict_recursion(element)}

    def RunOperation(self):
        try:
            #tree = ET.parse(self.filename)
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
            root = ET.fromstring(content)
            new_data = self.xml_to_dict(root)

            self.FetchData(new_data)
            self.ImportSuccessful()
        except Exception as e:
            raise Exception(f"{Const.GET_ERROR('ERROR_IMPXML')} {str(e)}")