from abc import ABC, abstractmethod
from ImpExp import ImpExp 
from Const import Const 
import json

class ImpJSON(ImpExp):
    def __init__(self, filename):
        super().__init__(filename)

    def RunOperation(self):
        try:
            with open(self.filename, 'r') as file:
                new_data = json.load(file)
                
            self.FetchData(new_data)
            self.ImportSuccessful()
        except Exception as e:
            raise Exception(f"{Const.GET_ERROR('ERROR_IMPJSON')} {str(e)}")