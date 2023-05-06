"""
    Factory 
    - Factory is a creational design pattern that provides an interface for creating objects
    in a superclass, but allows subclasses to alter the type of objects that will be created.

    3 Components => 1. creator 2. product 3. client

    creators are deciding what kind of objects should be created. (File, JsonFile, XmlFile)
    products are doing the actual functioality. In the example below, Json ans Xml classes are products.
    client is dealing with client request. (like client function below)
"""

from abc import ABC, abstractmethod

class File(ABC): # creator
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def make(self):
        pass

    def call_edit(self):
        product = self.make()
        result = product.edit(self.file)
        return result


# JsonFile and XmlFile classes are changing the Type of File Object

class JsonFile(File): # creator
    def make(self,):
        return Json()
    
class XmlFile(File): # creator
    def make(self,):
        return Xml()

class Json:    # product
    def edit(self, file):
        return f'Working on {file} json...'

class Xml:   # product
    def edit(self, file):
        return f'Working on {file} xml...'


def client(file, format): # client
    formats = {
        'json': JsonFile,
        'xml': XmlFile,
    }
    result = formats[format](file)
    return result.call_edit()

print(client('filename', 'json'))

