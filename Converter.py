import sys
import os
from Const import Const 
from ImpExp import ImpExp 
from ImpJSON import ImpJSON 
from ExpJSON import ExpJSON
from ImpYML import ImpYML
from ExpYML import ExpYML

#from AllImpExp import *

class Converter:
    inputFilePath       = ''
    inputFileFormat     = ''
    outputFilePath      = ''
    outputFileFormat    = ''
    supportedFormats    = list()
    

    def __init__(self, inputFile, outputFile, processImmediately = True):
        # initialize supported formats
        self.supportedFormats = [Const.GET_VALUE('TYPE_XML'), Const.GET_VALUE('TYPE_YML'), Const.GET_VALUE('TYPE_JSON')]

        # check if file exists
        Converter.checkIfFileExists(inputFile)
        #Converter.checkIfFileExists(outputFile)
        
        #write to fields
        self.inputFilePath      = inputFile
        self.outputFilePath     = outputFile
        self.inputFileFormat    = Converter.extractFileFormat(self.inputFilePath)
        self.outputFileFormat   = Converter.extractFileFormat(self.outputFilePath)

        #check if file format supported
        self.checkIfFormatSupported(self.inputFileFormat)
        self.checkIfFormatSupported(self.outputFileFormat)

        if processImmediately:
            self.Convert()


    def checkIfFileExists(file):
        if not os.path.exists(file):
            raise Exception(f'{Const.GET_ERROR("MISSING_FILE")}: {file}')

    def checkIfFormatSupported(self, format):
        if format not in self.supportedFormats:
            raise Exception(f'{Const.GET_ERROR("UNKNOWN_FORMAT")}: {format}')

    def extractFileFormat(file):
        try:
            x = file.split('.')
            print(x)
            print(f'extractFileFormat: extracted {x[-1].lower()}')
            return x[-1].lower()
        except Exception as err:
            raise Exception(f'{Const.GET_ERROR("OTHER_EXCEPTION")}: {err=}, {type(err)=}')

    def Convert(self):
        #importer = ImpExp(self.inputFilePath)
        #exporter = ImpExp(outputFile)

        if self.inputFileFormat   == Const.GET_VALUE('TYPE_XML'):
            importer = ImpXML(self.inputFilePath)
        elif self.inputFileFormat == Const.GET_VALUE('TYPE_YML'):
            importer = ImpYML(self.inputFilePath)
        elif self.inputFileFormat == Const.GET_VALUE('TYPE_JSON'):
            importer = ImpJSON(self.inputFilePath)
        else:
            raise Exception(f'{Const.GET_ERROR("UNKNOWN_FORMAT")}: {self.inputFilePath}')

        if self.outputFileFormat   == Const.GET_VALUE('TYPE_XML'):
            exporter = ExpXML(self.outputFilePath)
        elif self.outputFileFormat == Const.GET_VALUE('TYPE_YML'):
            exporter = ExpYML(self.outputFilePath)
        elif self.outputFileFormat == Const.GET_VALUE('TYPE_JSON'):
            exporter = ExpJSON(self.outputFilePath)
        else:
            raise Exception(f'{Const.GET_ERROR("UNKNOWN_FORMAT")}: {self.inputFilePath}')

        importer.RunOperation()
        exporter.FetchData( importer.ExtractData() )
        exporter.RunOperation()




if __name__ == '__main__':
    argumentList = sys.argv[1:]

    if not len(argumentList) == 2:
        print(Const.GET_TEXT('USAGE'))
        raise Exception(Const.GET_ERROR('INVALID_NO_OF_ARGS'))
    
    converter = Converter(argumentList[0], argumentList[1])
