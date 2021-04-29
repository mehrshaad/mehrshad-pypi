########## Wrote by Mehrshad! ##########
import json


class Json:
    def __init__(self, fileName: str, filePath: str = ''):
        self.filePath = filePath
        self.fileName = fileName
        self.data = {}
        if len(self.fileName) > 5:
            if self.fileName[-5:] != '.json':
                self.fileName += '.json'
        else:
            self.fileName += '.json'

        if self.filePath != '':
            if self.filePath[-1] != '/':
                self.filePath += '/'
            self.fileName = self.filePath + self.fileName

    def __str__(self):
        return str(self.data)

    def createJson(self):
        try:
            json_file = open(self.fileName, 'a+')
            return 'done!'
        except:
            raise Exception(
                f"Mehrshad.FileManage.Json.createJson('{self.fileName}') Error: unknown!")

    def readFrom(self, get_keys: bool = False):
        try:
            with open(self.fileName) as json_file:
                self.data = json.load(json_file)

            if get_keys:
                return self.data, list(self.data.keys())
            return self.data
        except FileNotFoundError:
            raise Exception(
                f"Mehrshad.FileManage.Json.readFrom('{self.fileName}') Error: '{self.fileName}' does not exist!")
        except json.decoder.JSONDecodeError:
            raise Exception(
                f"Mehrshad.FileManage.Json.readFrom('{self.fileName}') Error: '{self.fileName}' is empty!")
        except:
            raise Exception(
                f"Mehrshad.FileManage.Json.readFrom('{self.fileName}') Error: unknown!")

    def writeTo(self, data: dict, indent: int = 4, sort_keys: bool = True):
        try:
            with open(self.fileName, 'w') as json_file:
                json.dump(data, json_file, indent=indent, sort_keys=sort_keys)
            return 'done!'
        except FileNotFoundError:
            raise Exception(
                f"Mehrshad.FileManage.Json.writeTo('{self.fileName}') Error: '{self.fileName}' does not exist!")
        except:
            raise Exception(
                f"Mehrshad.FileManage.Json.writeTo('{self.fileName}') Error: unknown!")
