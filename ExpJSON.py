from abc import ABC, abstractmethod
import json
from ImpExp import ImpExp 
from Const import Const 

class ExpJSON(ImpExp):
    def __init__(self, filename):
        super().__init__(filename)

    def RunOperation(self):
        try:
            with open(self.filename, 'w+') as file:
                json.dump(self.data, file, indent=4)
            self.ImportSuccessful()
        except Exception as e:
            raise Exception(f"{Const.GET_ERROR('ERROR_EXPJSON')} {str(e)}")