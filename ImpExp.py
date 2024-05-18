from abc import ABC, abstractmethod

class ImpExp(ABC):
    data     = dict()
    filename = ''
    isReady  = False

    def __init__(self, filename):
        self.filename = filename
        self.isReady  = False

    @abstractmethod
    def RunOperation(self):
        raise Exception(Const.GET_ERROR('RUN_OPERATION_UNDEFINED'))

    def ImportSuccessful(self):
        self.isReady = True

    def FetchData(self, new_data):
        self.data = new_data
    
    def ExtractData(self):
        return self.data