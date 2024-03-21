# Import the abc module, which provides infrastructure for defining abstract base classes (ABCs)
import abc

class MedicalDocParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text   # Initialize the MedicalDocParser class with text data


    @abc.abstractmethod
    def parse(self):
        # Define an abstract method parse() that should be implemented by subclasses
        pass