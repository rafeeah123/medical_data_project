import pytest

from backend.src.parser_patient_details import PatientDetailsParser

# Define a fixture for a document with patient details for testing
@pytest.fixture()
def doc_1_kathy():
    document_text = '''
    Patient Medical Record . : :

    Patient Information


    Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight:
    9264 Ash Dr 95
    New York City, 10005 a
    United States Height:
    190
    In Case of Emergency
    ee oe
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone
    Genera! Medical History
    I i
    Chicken Pox (Varicella): Measies:
    IMMUNE IMMUNE

    Have you had the Hepatitis B vaccination?

    No

    List any Medical Problems (asthma, seizures, headaches):

    Migraine
    '''

    return PatientDetailsParser(document_text)

# Define a fixture for another document with patient details for testing
@pytest.fixture()
def doc_2_jerry():
    document_text = '''
    Patient Medical Record

    Patient Information
    Jerry Lucas

    (279) 920-8204

    4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    United States

    In Case of Emergency

    -_ OCC OO eee

    Joe Lucas

    Home phone

    General Medical History



    Chicken Pox (Varicelia):
    IMMUNE
    Have you had the Hepatitis B vaccination?

    Yes”

    Birth Date
    May 2 1998

    Weight:
    57

    Height:
    170

    4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    United States

    Work phone

    Measles: .

    NOT IMMUNE

    List any Medical Problems (asthma, seizures, headaches):

    N/A
        '''
    return PatientDetailsParser(document_text)

# Define tests for extracting patient name from the document
def test_get_patient_name(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_patient_name() == 'Kathy Crawford'
    assert doc_2_jerry.get_patient_name() == 'Jerry Lucas'

# Define tests for extracting patient phone number from the document
def test_get_patient_phone_number(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_patient_phone_number() == '(737) 988-0851'
    assert doc_2_jerry.get_patient_phone_number() == '(279) 920-8204'

# Define tests for extracting hepatitis B vaccination status from the document
def test_get_hepatitis_b_vaccination(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_hepatitis_b_vaccination() == 'No'
    assert doc_2_jerry.get_hepatitis_b_vaccination() == 'Yes'

# Define tests for extracting medical problems from the document
def test_get_medical_problems(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_medical_problems() == 'Migraine'
    assert doc_2_jerry.get_medical_problems() == 'N/A'

# Define tests for parsing the document and extracting patient details
def test_parse(doc_1_kathy, doc_2_jerry):
    record_kathy = doc_1_kathy.parse()
    assert record_kathy['patient_name'] == 'Kathy Crawford'
    assert record_kathy['phone_number'] == '(737) 988-0851'
    assert record_kathy['medical_problems'] == 'Migraine'
    assert record_kathy['hepatitis_b_vaccination'] == 'No'


    record_jerry = doc_2_jerry.parse()
    assert record_jerry['patient_name'] == 'Jerry Lucas'
    assert record_jerry['phone_number'] == '(279) 920-8204'
    assert record_jerry['medical_problems'] == 'N/A'
    assert record_jerry['hepatitis_b_vaccination'] == 'Yes'