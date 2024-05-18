import json

class JSONLoader:
    def __init__(self, filePath):
        self.filePath = filePath
        self.data = None
    
    def LoadFile(self, filePath):
        if filePath:
            self.filePath = filePath
        
        if not self.filePath:
            raise ValueError("File path not provided")
        
        try:
            with open(self.filePath, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                print(f"JSON file '{self.filePath}' loaded successfully.")
        except FileNotFoundError:
            print(f"File not found: {self.filePath}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def GetValue(self, key):
        if self.data is not None:
            return self.data.get(key, None)
        return None
    
    def GetKeys(self):
        if self.data is not None:
            return list(self.data.keys())
        return []
