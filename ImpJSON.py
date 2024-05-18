from abc import ABC, abstractmethod
import ImpExp

class ImpJSON(ImpExp):

    def __init__(self,filename):
        super().__init__(filename)
