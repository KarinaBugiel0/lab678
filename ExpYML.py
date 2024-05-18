from abc import ABC, abstractmethod
import ImpExp

class ExpYML(ImpExp):

    def __init__(self,filename):
        super().__init__(filename)
