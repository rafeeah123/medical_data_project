from pdf2image import convert_from_path  # Library for converting PDF to images
import pytesseract  # Optical Character Recognition (OCR) tool
import util  # Custom utility functions

from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser

# Path to the Poppler binary for pdf2image library
POPPLER_PATH = r'C:\poppler-24.02.0\Library\bin'

# Path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Function to extract information from a PDF file based on its format
def extract(file_path, file_format):
    # Extracting text from pdf file
    #Step 1 : Convert pdf to image
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    # Check if there are pages available
    if len(pages)>0:
        page = pages[0]  # Select the first page
        #Preprocess the image for better OCR accuracy
        processed_image = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng') # Perform OCR on the image
        document_text = '\n' + text  # Add extracted text to the document text variable

    # step 2: extract fields from text
    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data

if __name__ == '__main__':

    # Extract prescription details from sample prescription PDF files
    prescription_data1 = extract('../resources/prescription/pre_1.pdf', 'prescription')
    prescription_data2 = extract('../resources/prescription/pre_2.pdf', 'prescription')

    print(f"Prescription Details 1 : \n  {prescription_data1}")
    print(f"Prescription Details 2 : \n  {prescription_data2}")

    # Extract patient details from sample patient details PDF files
    patient_data1 = extract('../resources/patient_details/pd_1.pdf', 'patient_details')
    patient_data2 = extract('../resources/patient_details/pd_2.pdf', 'patient_details')

    print(f"Patient Details 1 : \n  {patient_data1}")
    print(f"Patient Details 2 : \n  {patient_data2}")
