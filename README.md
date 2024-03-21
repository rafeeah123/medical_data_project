# Extracting Medical Data from Documents
This project aims to extract structured data from medical documents such as prescriptions and patient details using a combination of OCR, computer vision and pattern-matching techniques integrated with Fast API.

## Overview

The Medical Data Extractor consists of several components:

1.PDF to Image Conversion: Utilizes the pdf2image library to convert PDF documents into images, enabling further processing.

2.Enhancing Readability: Employs OpenCV for computer vision tasks, including image preprocessing with techniques such as adaptive thresholding, improving image quality and readability.

3.Text Extraction: Utilizes pytesseract to extract text from images, converting the document's content into a readable format.

4.Pattern Matching: Utilizes regular expressions (regex) to match patterns and extract relevant information from the extracted text.

5.FastAPI Integration: Integrates FastAPI to expose endpoints for handling HTTP requests, allowing users to upload medical documents and receive extracted data in JSON format.

6.Testing with Pytest: Uses Pytest for automated testing to ensure the correctness and reliability of the extraction process.

## Getting Started:

To get started with the Medical Data Extractor, follow these steps:

1.Clone the repository: git clone <repository_url>

2.Install the required dependencies: pip install -r requirements.txt

3.Run the FastAPI server by ruuning the 'main.py' file
4.Access the API endpoints and upload medical documents to extract data.

## Tools and Technologies Used:

### Tools:

1.IDE - PyCharm

2.Postman

### Technologies:

    Backend:

    Python

    Libraries :

    Pdf2image
    Opencv
    Pytesseract
    Regex
    Fast API
    pytest

    Frontend:

    HTML
    CSS
    Javascript


## Learnings:

1.OCR: OCR techniques to extract text from images, enabling conversion of medical documents into machine-readable formats.

2.Computer Vision: Developed skills in image preprocessing, enhancement, and feature extraction using OpenCV library for better readability and analysis of medical documents.

3.FastAPI: Explored the FastAPI framework for building efficient and scalable web APIs, facilitating seamless integration of backend services for document processing and data extraction.

4.PyTest: Utilized PyTest for automated testing, ensuring reliability and correctness of code implementations, particularly in verifying accuracy of extracted data from medical documents.

5.Pattern Matching: Gained proficiency in using regular expressions (regex) for precise identification and retrieval of specific information from unstructured text data.

6.HTTP Request-Response Handling: Implemented HTTP request-response handling using FastAPI endpoints, facilitating communication between frontend and backend components of the application and enabling data exchange in JSON format.

7.Debugging and Troubleshooting: Developed skills in debugging and troubleshooting techniques, resolving issues related to image processing, text extraction, and API integration, enhancing overall project robustness and reliability.


## Future Enhancements:

1.Improve accuracy and robustness of text extraction through machine learning techniques.

2.Enhance preprocessing methods to handle a wider range of document formats and qualities.

3.Implement additional features for document classification and data validation.

## Feedback

Your feedback is valuable to me in my learning journey. Please feel free to text me on Linkedin with your thoughts and suggestions.
Linkedin URL : https://www.linkedin.com/in/rafeeahramzan/






