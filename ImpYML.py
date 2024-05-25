from abc import ABC, abstractmethod
from ImpExp import ImpExp 
import yaml

class ImpYML(ImpExp):
    def __init__(self, filename):
        super().__init__(filename)

