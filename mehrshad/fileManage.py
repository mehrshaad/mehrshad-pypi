"""
mehrshad.fileManage:
===
 huge thanks for using my package!
 this is the fileManage file of my package.
 it provides all of my classes that built for file managing.
    
naming:
---
 i used camelCase for nameing functions,
 and PascalCase for naming classes.

class names in this file:
---
 Json: this class will let you manage everything about json files very easily! you can create, write, save, update and etc.
 Excel: coming soon ...
 SQL: coming soon ...
 Text: coming soon ...
    
note:
---
 please report any bug, suggestion, idea and etc.
 
credits:
---
 arthur: (Ali) Mehrshad Dadashzadeh
 github: https://github.com/mehrshaad/mehrshad-pypi
 linkedIn: https://www.linkedin.com/in/mehrshad-dadashzadeh-7053491b3
 pypi: https://pypi.org/project/mehrshad
"""
import os as M1
import json as M2


class Json:
    """this is the Json class. you can use it for managing json files.
    everything you need for managing your data with a json file, is in here!
    
    NOTE: you can only enter file name as filePath argument.
    ---
    
    Functions:
    ---
    + readFrom(getKeys: bool = False)
    + updateData(data: dict = {}, replaceData: bool = False, writeTo: bool = False)
    + updateFile(indent: int = 4, sortKeys: bool = True)
    + writeTo(data: dict, indent: int = 4, sortKeys: bool = True)
    
    Methods:
    ---
    + you can use '+' sign between a Json object and dict, and that will create a new Json object with updated data (dict).
    + you can use '+=' between a Json object and dict, and it will update the current data of Json object.
    """
    def __init__(self,
                 filePath: str,
                 data: dict = {},
                 createFile: bool = True):
        filePath = filePath.strip().replace('\\', '/')
        if filePath == '' or filePath.split('/')[-1] == '':
            raise RuntimeError(
                f"Mehrshad.FileManage.Json.readFrom('{filePath}') Error: '{filePath}' is not a proper name!"
            )
        if filePath[0] == '/': filePath = filePath[1:]
        if filePath[-1] == '/': filePath = filePath[:-1]
        self.__fileName = filePath
        if len(self.__fileName) > 5:
            if self.__fileName[-5:] != '.json':
                self.__fileName += '.json'
        else:
            self.__fileName += '.json'
        try:
            self.__data = self.readFrom()
            self.updateData(data)
            self.updateFile()
        except:
            self.__data = data
            if createFile:
                self.__createJson(self.__data)

    def __str__(self):
        return str(self.__data)

    def __add__(self, data: dict):
        temp = self.__copy__()
        temp.__data = self.__data.copy()
        temp.updateData(data)
        return temp

    def __iadd__(self, data: dict):
        self.updateData(data)
        return self

    def __copy__(self):
        return type(self)(self.__fileName)

    def __createJson(self, data: dict = {}):
        """this function is used for creating a json file based on the name and
        address you entered in when you were creating a Json object.

        Args:
            data (dict, optional): you can input the data you want to place in the json file. Defaults to {}.

        Raises:
            Exception: if anything unknown happens! for the most common errors it got solutions.

        Returns:
            str: status of works at the end.
        """
        try:
            open(self.__fileName, 'a+')
            if data != {}:
                self.updateData(data, writeTo=True)
            return f"Mehrshad.FileManage.Json.__createJson({self.__fileName}) Successful!"
        except (FileNotFoundError, PermissionError):
            temp = '/'.join(self.__fileName.split('/')[:-1])
            M1.makedirs(temp)
            return self.__createJson(data)
        except:
            raise Exception(
                f"Mehrshad.FileManage.Json.__createJson({self.__fileName}) Error: unknown!"
            )

    def clearFile(self):
        """use this function if you wand to clear all data from a json file.

        Raises:
            RuntimeError: this error happens if the file isn't found.
            Exception: if anything unknown happens! for the most common errors it got solutions.

        Returns:
            str: status of works at the end.
        """
        try:
            self.writeTo({})
            self.__data = {}
            return f"Mehrshad.FileManage.Json.clearFile({self.__fileName}) Successful!"
        except FileNotFoundError:
            raise RuntimeError(
                f"Mehrshad.FileManage.Json.clearFile({self.__fileName}) Error: {self.__fileName} does not exist!"
            )
        except:
            raise Exception(
                f"Mehrshad.FileManage.Json.clearFile({self.__fileName}) Error: unknown!"
            )

    def readFrom(self, getKeys: bool = False):
        """call this function when you want to read all
        data from the json file you created a Json object with.

        Args:
            getKeys (bool, optional): set it to True if you want to get the list of keys. Defaults to False.

        Raises:
            RuntimeError: this error happens if the file isn't found.
            UnicodeError: this error raises if the json file is empty!
            Exception: if anything unknown happens! for the most common errors it got solutions.

        Returns:
            dict: the read data from json file. (if you set getKeys to True a list will return too)
        """
        try:
            with open(self.__fileName) as json_file:
                self.__data = M2.load(json_file)

            if getKeys:
                return self.__data, list(self.__data.keys())
            return self.__data
        except FileNotFoundError:
            raise RuntimeError(
                f"Mehrshad.FileManage.Json.readFrom({self.__fileName}) Error: {self.__fileName} does not exist!"
            )
        except M2.decoder.JSONDecodeError:
            raise UnicodeError(
                f"Mehrshad.FileManage.Json.readFrom({self.__fileName}) Error: {self.__fileName} is empty!"
            )
        except:
            raise Exception(
                f"Mehrshad.FileManage.Json.readFrom({self.__fileName}) Error: unknown!"
            )

    def updateData(self,
                   data: dict,
                   replaceData: bool = False,
                   writeTo: bool = False):
        """you can update/replace existed data with something you entered.

        Args:
            data (dict): the data you want to update/replace the current data.
            replaceData (bool, optional): set it to True if you want to replace the current data with the data you entered. Defaults to False.
            writeTo (bool, optional): if you set this to True it will write to json file after updating/replacing data. Defaults to False.

        Raises:
            Exception: if anything unknown happens! for the most common errors it got solutions.

        Returns:
            str: status of works at the end.
        """
        try:
            if replaceData:
                self.__data = data
            else:
                self.__data.update(data)
            if writeTo:
                self.updateFile()
            return f"Mehrshad.FileManage.Json.updateData({data}) Successful!"
        except:
            raise Exception(
                f"Mehrshad.FileManage.Json.updateData({data}) Error: unknown!")

    def updateFile(self, indent: int = 4, sortKeys: bool = True):
        """this function is used for updating the json file with the data value
        in Json object.

        Args:
            indent (int, optional): the output json file length of tabs (indent). Defaults to 4.
            sortKeys (bool, optional): set if to False if you don't want to sort dict keys in json file. Defaults to True.

        Raises:
            RuntimeError: this error happens if the file isn't found.
            Exception: if anything unknown happens! for the most common errors it got solutions.

        Returns:
            str: status of works at the end.
        """
        try:
            with open(self.__fileName, 'w') as json_file:
                M2.dump(self.__data,
                        json_file,
                        indent=indent,
                        sort_keys=sortKeys)
            return f"Mehrshad.FileManage.Json.updateFile({self.__fileName}) Successful!"
        except FileNotFoundError:
            raise RuntimeError(
                f"Mehrshad.FileManage.Json.updateFile({self.__fileName}) Error: {self.__fileName} does not exist!"
            )
        except:
            raise Exception(
                f"Mehrshad.FileManage.Json.updateFile({self.__fileName}) Error: unknown!"
            )

    def writeTo(self, data: dict, indent: int = 4, sortKeys: bool = True):
        """you can use this function when want to replace all of json file data with
        some data you entered.

        Args:
            data (dict): the data you want to replace the current data of json file with.
            indent (int, optional): the output json file length of tabs (indent). Defaults to 4.
            sortKeys (bool, optional): set if to False if you don't want to sort dict keys in json file. Defaults to True.

        Raises:
            RuntimeError: this error happens if the file isn't found.
            Exception: if anything unknown happens! for the most common errors it got solutions.

        Returns:
            str: status of works at the end.
        """
        try:
            with open(self.__fileName, 'w') as json_file:
                M2.dump(data, json_file, indent=indent, sort_keys=sortKeys)
            return f"Mehrshad.FileManage.Json.writeTo({self.__fileName}) Successful!"
        except FileNotFoundError:
            raise RuntimeError(
                f"Mehrshad.FileManage.Json.writeTo({self.__fileName}) Error: {self.__fileName} does not exist!"
            )
        except:
            raise Exception(
                f"Mehrshad.FileManage.Json.writeTo({self.__fileName}) Error: unknown!"
            )
