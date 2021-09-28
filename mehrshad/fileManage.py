"""
mehrshad.fileManage module:
===
Thanks again for using my Python package, it means a lot to
me! This module will provide all of the file-managing classes which includes Json
and Text. Other class like Excel and Sql, will be added soon...
    
Naming:
---
+ Functions | Modules - camelCase
+ Classes - PascalCase

Class names in this file:
---
+ Json: This class will let you to manage everything about the json files very easily! You can create, write, save, update, etc.
+ Text: This is the Text class! You can create, edit, update, ... the txt files.
+ Excel: Coming soon...
+ Sql: Coming soon...
    
Note:
---
Please report any bug, suggestion, idea, etc.
 
Credits:
---
+ Author: (Ali) Mehrshad Dadashzadeh
+ GitHub: https://github.com/mehrshaad/mehrshad-pypi
+ LinkedIn: https://www.linkedin.com/in/mehrshad-dadashzadeh-7053491b3
+ PyPI: https://pypi.org/project/mehrshad
"""
import os as M1
import json as M2
from typing import Union as M3


class Json:
    """This is the Json class. You can use it for managing json files.
    Everything you need for managing your data with a json file, is here!
    It'll automatically creates a json file if it wasn't there already.
    
    Functions:
    ---
    + read(getKeys: bool = False)
    + update(data: dict = {}, replaceData: bool = False, write: bool = False)
    + save(indent: int = 4, sortKeys: bool = True)
    + write(data: dict, indent: int = 4, sortKeys: bool = True)
    
    Methods:
    ---
    + You can use '+' sign between a Json object and dict, and that will create a new Json object with updated data (dict).
    + You can use '+=' between a Json object and dict, and it will update the current data of Json object.
    """
    def __init__(self, filePath: str, data: dict = {}, autoSave: bool = True):
        filePath = filePath.strip().replace('\\', '/')
        if filePath == '' or filePath.split('/')[-1] == '':
            raise RuntimeError(
                f"Mehrshad.FileManage.Json('{filePath}') Error: '{filePath}' is not a proper name!"
            )
        if filePath[0] == '/': filePath = filePath[1:]
        if filePath[-1] == '/': filePath = filePath[:-1]
        self._fileName = filePath
        self._autoSave = autoSave
        if len(self._fileName) > 5:
            if self._fileName[-5:] != '.json':
                self._fileName += '.json'
        else:
            self._fileName += '.json'
        try:
            self._data = self.read()
        except:
            self._data = data
        self._create(data)
        self.save()

    def __str__(self):
        return str(self._data)

    def __add__(self, data: dict):
        temp = self._copy__()
        temp._data = self._data.copy()
        temp.update(data)
        return temp

    def __iadd__(self, data: dict):
        self.update(data)
        return self

    def __copy__(self):
        return type(self)(self._fileName)

    def _create(self, data: dict = {}):
        """This function is used for creating a json file based on the name and
        address you entered in when you were creating a Json object.

        Args:
            data (dict, optional): You can input the data you want to place in the json file. Defaults to {}.

        Raises:
            Exception: If anything unknown happens! For the most common errors it got solutions.

        Returns:
            str: Status of works at the end.
        """
        try:
            open(self._fileName, 'a+')
            if data != {}:
                self.update(data, write=True)
            return f"Mehrshad.FileManage.Json._create({self._fileName}) Successful!"
        except (FileNotFoundError, PermissionError):
            temp = '/'.join(self._fileName.split('/')[:-1])
            print(temp)
            M1.makedirs(temp)
            return self._create(data)
        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Json._create({self._fileName}) Error: {error}"
            )

    def clear(self):
        """Use this function if you wand to clear all the data from the json file.

        Raises:
            FileNotFoundError: This error happens if the file isn't found.
            Exception: If anything unknown happens! For the most common errors it got solutions.

        Returns:
            str: Status of works at the end.
        """
        try:
            self.write({})
            self._data = {}
            return f"Mehrshad.FileManage.Json.clear({self._fileName}) Successful!"
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Mehrshad.FileManage.Json.clear({self._fileName}) Error: {self._fileName} does not exist!"
            )
        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Json.clear({self._fileName}) Error: {error}"
            )

    def read(self, getKeys: bool = False):
        """Call this function when you want to read all
        data from the json file you created a Json object with.

        Args:
            getKeys (bool, optional): Set it to True if you want to get the list of keys. Defaults to False.

        Raises:
            RuntimeError: This error happens if the file isn't found.
            UnicodeError: This error raises if the json file is empty!
            Exception: If anything unknown happens! For the most common errors it got solutions.

        Returns:
            dict: The read data from json file. (If you set getKeys to True a list will return too)
        """
        try:
            with open(self._fileName, 'r') as json_file:
                self._data = M2.load(json_file)

            if getKeys:
                return self._data, list(self._data.keys())
            return self._data
        except FileNotFoundError:
            raise RuntimeError(
                f"Mehrshad.FileManage.Json.read({self._fileName}) Error: {self._fileName} does not exist!"
            )
        except M2.decoder.JSONDecodeError:
            raise UnicodeError(
                f"Mehrshad.FileManage.Json.read({self._fileName}) Error: {self._fileName} is empty!"
            )
        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Json.read({self._fileName}) Error: {error}"
            )

    def update(self,
               data: dict,
               replaceData: bool = False,
               write: bool = False):
        """You can update/replace the existed data with some data you entered.

        Args:
            data (dict): The data you want to update/replace the current data.
            replaceData (bool, optional): Set it to True if you want to replace the current data with the data you entered. Defaults to False.
            write (bool, optional): If you set this to True it will write to json file after updating/replacing data. Defaults to False.

        Raises:
            Exception: If anything unknown happens! For the most common errors it got solutions.

        Returns:
            str: Status of works at the end.
        """
        try:
            if replaceData:
                self._data = data
            else:
                self._data.update(data)
            if write or self._autoSave:
                self.save()
            return f"Mehrshad.FileManage.Json.update({data}) Successful!"
        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Json.update({data}) Error: {error}")

    def save(self, indent: int = 4, sortKeys: bool = True):
        """This function is used for updating the json file with the data value
        in Json object.

        Args:
            indent (int, optional): The length of the output json file tabs (indent). Defaults to 4.
            sortKeys (bool, optional): Set if to False if you don't want to sort dict keys in json file. Defaults to True.

        Raises:
            RuntimeError: This error happens if the file isn't found.
            Exception: If anything unknown happens! For the most common errors it got solutions.

        Returns:
            str: Status of works at the end.
        """
        try:
            with open(self._fileName, 'w') as json_file:
                M2.dump(self._data,
                        json_file,
                        indent=indent,
                        sort_keys=sortKeys)
            return f"Mehrshad.FileManage.Json.save({self._fileName}) Successful!"
        except FileNotFoundError:
            raise RuntimeError(
                f"Mehrshad.FileManage.Json.save({self._fileName}) Error: {self._fileName} does not exist!"
            )
        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Json.save({self._fileName}) Error: {error}"
            )

    def write(self, data: dict, indent: int = 4, sortKeys: bool = True):
        """You can use this function when want to replace all of the json file's data with
        some data you just entered.

        Args:
            data (dict): The data you want to replace the current data of json file with.
            indent (int, optional): The output json file length of tabs (indent). Defaults to 4.
            sortKeys (bool, optional): Set if to False if you don't want to sort dict keys in json file. Defaults to True.

        Raises:
            RuntimeError: This error happens if the file isn't found.
            Exception: If anything unknown happens! For the most common errors it got solutions.

        Returns:
            str: Status of works at the end.
        """
        try:
            with open(self._fileName, 'w') as json_file:
                M2.dump(data, json_file, indent=indent, sort_keys=sortKeys)
            return f"Mehrshad.FileManage.Json.write({self._fileName}) Successful!"
        except FileNotFoundError:
            raise RuntimeError(
                f"Mehrshad.FileManage.Json.write({self._fileName}) Error: {self._fileName} does not exist!"
            )
        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Json.write({self._fileName}) Error: {error}"
            )


class Text:
    """This is the Text class! You can create, edit, update, ... the txt files.
    The txt file will be automatically created if it doesn't already exist. You
    can add your data by using the update function.
    
    Functions:
    ---
    + read()
    + save()
    + clear()
    + update(data: str, list, dict, int = '', save: bool = False, overwrite: bool = False, newLine: bool = False)
    
    Methods:
    ---
    + You can change the address of the txt file by using address method and adding a str that show the path of file.
    + You can use '+=' between a Text object and str, then it'll updates the txt file data.
    """
    def __init__(self, filePath: str, autoSave: bool = True):
        """

        Args:
            filePath (str): [description]
            autoSave (bool, optional): [description]. Defaults to True.

        Raises:
            RuntimeError: [description]
        """
        filePath = filePath.strip().replace('\\', '/')
        if filePath == '' or filePath.split('/')[-1] == '':
            raise RuntimeError(
                f"Mehrshad.FileManage.Text('{filePath}') Error: '{filePath}' is not a proper name!"
            )
        if filePath[0] == '/': filePath = filePath[1:]
        if filePath[-1] == '/': filePath = filePath[:-1]
        self._fileName = filePath
        self._autoSave = autoSave
        if len(self._fileName) > 4:
            if self._fileName[-4:] != '.txt':
                self._fileName += '.txt'
        else:
            self._fileName += '.txt'

        try:
            self._data = self.read()
        except:
            self._data = ''
            self._create(self._data)

    def __str__(self):
        return str(self._data)

    def __iadd__(self, data):
        self.update(data)
        return self

    def __copy__(self):
        return type(self)(self._fileName)

    def _create(self, data=''):
        """This function is used for creating a txt file based on the name and
        address you entered in, when you were creating a Text object.

        Args:
            data (str, optional): You can input the data you want to place in the txt file. Defaults to ''.

        Raises:
            Exception: If anything unknown happens!

        Returns:
            str: Result of the function.
        """
        try:
            open(self._fileName, 'a+')
            if data != '' and data != [] and data != {}:
                self.update(data, save=True)
            return f"Mehrshad.FileManage.Text._create({self._fileName}) Successful!"

        except (FileNotFoundError, PermissionError):
            temp = '/'.join(self._fileName.split('/')[:-1])
            M1.makedirs(temp)
            self._create(data)

        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Text._create({self._fileName}) Error: {error}"
            )

    def clear(self):
        """Use this function if you wand to clear all data from a txt file.

        Raises:
            FileNotFoundError: This error happens if the file isn't found.
            Exception: If anything unknown happens! For the most common errors it got solutions.

        Returns:
            str: Status of works at the end.
        """
        try:
            temp = open(self._fileName, 'a+')
            temp.truncate(0)
            self._data = ''
            return f"Mehrshad.FileManage.Text.clear({self._fileName}) Successful!"
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Mehrshad.FileManage.Text.clear({self._fileName}) Error: {self._fileName} does not exist!"
            )
        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Text.clear({self._fileName}) Error: {error}"
            )

    def read(self):
        """Call this function when you want to read all
        data from the txt file you created a Text object with, or
        update the existing data.

        Raises:
            RuntimeError: This error happens if the file isn't found.
            Exception: If anything unknown happens! For the most of the common errors it got solutions.

        Returns:
            str: The read data from txt file.
        """
        try:
            with open(self._fileName, 'r') as txt_file:
                self._data = txt_file.read()
            return self._data

        except FileNotFoundError:
            raise RuntimeError(
                f"Mehrshad.FileManage.Text.read({self._fileName}) Error: {self._fileName} does not exist!"
            )

        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Text.read({self._fileName}) Error: {error}"
            )

    def update(self,
               data: M3[str, list, dict, int],
               save: bool = False,
               overwrite: bool = False,
               newLine: bool = False):
        """This function is used for updating or replacing the data of the Text object.

        Args:
            data (str | list | dict | int): The data you want to add or replace.
            save (bool, optional): A boolean that decides whether the file'll be saved or not. Defaults to False.
            overwrite (bool, optional): Set it to True in order to replace the existing data. Defaults to False.
            newLine (bool, optional): By setting it to True, added data will be written in the next line. Defaults to False.

        Raises:
            Exception: If anything uncommon happens!

        Returns:
            str: As a result of function works.
        """
        try:
            data = str(data)
            if newLine:
                data = '\n' + data
            if overwrite:
                self._data = data
            else:
                self._data += data
            if save or self._autoSave:
                self.save()
            return f"Mehrshad.FileManage.Text.update({data}) Successful!"

        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Text.update({data}) Error: {error}")

    @property
    def address(self):
        return self._fileName

    @address.setter
    def address(self, filePath: str):
        filePath = filePath.strip().replace('\\', '/')
        if filePath == '' or filePath.split('/')[-1] == '':
            raise RuntimeError(
                f"Mehrshad.FileManage.Text.path('{filePath}') Error: '{filePath}' is not a proper name!"
            )
        if filePath[0] == '/': filePath = filePath[1:]
        if filePath[-1] == '/': filePath = filePath[:-1]
        self._fileName = filePath
        if len(self._fileName) > 4:
            if self._fileName[-4:] != '.txt':
                self._fileName += '.txt'
        else:
            self._fileName += '.txt'

        try:
            self._data = self.read()
        except:
            self._data = ''
            self._create(self._data)

    def save(self):
        """This function will save the txt file.

        Raises:
            RuntimeError: This error happens if the file isn't found.
            Exception: If anything unknown happens! For the most common errors it got solutions.

        Returns:
            str: Status of function works.
        """
        try:
            with open(self._fileName, 'w') as txt_file:
                txt_file.write(self._data)
            return f"Mehrshad.FileManage.Text.save({self._fileName}) Successful!"
        except FileNotFoundError:
            raise RuntimeError(
                f"Mehrshad.FileManage.Text.save({self._fileName}) Error: {self._fileName} does not exist!"
            )
        except Exception as error:
            raise Exception(
                f"Mehrshad.FileManage.Text.save({self._fileName}) Error: {error}"
            )