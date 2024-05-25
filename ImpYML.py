from abc import ABC, abstractmethod
from ImpExp import ImpExp 
import yaml

class ImpYML(ImpExp):
    def __init__(self, filename):
        super().__init__(filename)

    def RunOperation(self):
        try:
            with open(self.filename, 'r') as file:
                new_data = yaml.safe_load(file)
                
            self.FetchData(new_data)
            self.ImportSuccessful()
        except Exception as e:
            raise Exception(f"{Const.GET_ERROR('ERROR_IMPYML')} {str(e)}")