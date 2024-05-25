from abc import ABC, abstractmethod

class Const(object):

    values     =  {'TYPE_XML'      : 'xml',
                        'TYPE_YML'      : 'yml',
                        'TYPE_JSON'     : 'json'} 
    
    errors     =  {'UNKNOWN_FORMAT'            : 'File format not supported',
                        'MISSING_FILE'              : 'File is missing',
                        'UNKNOWN_CONST'             : 'Unknown constant value',
                        'OTHER_EXCEPTION'           : 'Unexpected exception',
                        'INVALID_NO_OF_ARGS'        : 'Invalid number of arguments, expected 2',
                        'RUN_OPERATION_UNDEFINED'   : 'Run operation in class of parent ImpExp has failed, because it was not defined. Please check Converter.Convert method',
                        'ERROR_IMPJSON'             : 'Error parsing JSON!',
                        'ERROR_IMPYML'              : 'Error parsing YML!',
                        'ERROR_IMPXML'              : 'Error parsing XML!',
                        'ERROR_EXPJSON'             : 'Error exporting to JSON!',
                        'ERROR_EXPYML'              : 'Error exporting to YML!',
                        'ERROR_EXPXML'              : 'Error exporting to XML!'}

    text       =  {'USAGE'       : 'Usage: converter.py <inputfile> <outputfile>'}


    @staticmethod
    def GET_VALUE(key):
        return Const.GET(key, Const.values, 'values')

    @staticmethod
    def GET_ERROR(key):
        return Const.GET(key, Const.errors, 'errors')

    @staticmethod
    def GET_TEXT(key):
        return Const.GET(key, Const.text, 'text')

    @staticmethod
    def GET(key, my_dict, dict_name):
        if key in my_dict:
            return my_dict[key]
        else:
            raise Exception(f'{Const.errors["UNKNOWN_CONST"]}: {key} in {dict_name}')

