from abc import ABC, abstractmethod
import ImpExp

class ExpJSON(ImpExp):

    def __init__(self,filename):
        super().__init__(filename)
