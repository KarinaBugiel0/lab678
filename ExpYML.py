from abc import ABC, abstractmethod
from ImpExp import ImpExp 
import yaml

class ExpYML(ImpExp):
    def __init__(self, filename):
        super().__init__(filename)

    def RunOperation(self):
        try:
            with open(self.filename, 'w') as file:
                yaml.dump(self.data, file, default_flow_style=False)
            self.ImportSuccessful()
        except Exception as e:
            raise Exception(f"{Const.GET_ERROR('ERROR_EXPYML')} {str(e)}")