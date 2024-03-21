import re

# Import the MedicalDocParser class from the parser_generic module
from backend.src.parser_generic import MedicalDocParser

# Define a subclass of MedicalDocParser for parsing prescription details
class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)
    # Method to parse prescription details from the text
    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address': self.get_field('patient_address'),
            'medicines': self.get_field('medicines'),
            'directions': self.get_field('directions'),
            'refills': self.get_field('refills')
        }

# Method to extract a specific field from the text using a predefined pattern
    def get_field(self, field_name):
        pattern_dict = {
            # Define patterns and flags for each field
            'patient_name': {'pattern': 'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'refills': {'pattern': 'Refill:(.*)times', 'flags': 0},
        }
        # Get the pattern object for the specified field
        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            # Use re.findall() to search for the pattern in the text
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()


# Test the parser with sample document text
if __name__ == '__main__':
    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222
Name: Marta Sharapova Date: 5/11/2022
Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram
Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks -
Lialda - take 2 pill everyday for 1 month
Refill: 3 times
'''
    pp = PrescriptionParser(document_text)
    print(pp.parse())