# Import necessary modules from FastAPI and other dependencies
from fastapi import FastAPI, File, UploadFile, Form, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Import the extraction function from the extractor module
from extractor import extract

# Import necessary modules for file handling and directory management
import uuid
import os

# Create a FastAPI app instance
app = FastAPI()

# Define the path to the frontend static files
frontend_static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend", "static"))

# Mount the frontend directory as static files accessible via "/static" URL
app.mount("/static", StaticFiles(directory=frontend_static_path), name="static")

# Define the current directory and the directory for uploaded files
current_dir = os.path.abspath(os.path.dirname(__file__))
uploads_dir = os.path.join(current_dir, '..', 'uploads')

# Create the directory if it doesn't exist
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)
    print("Uploads directory created successfully.")

# Define the endpoint for serving the index.html file
@app.get("/", response_class=FileResponse)
async def get_index():
    index_html_path = os.path.join(frontend_static_path, "index.html")
    if os.path.exists(index_html_path):
        return FileResponse(index_html_path)
    else:
        return {"error": "Index HTML file not found"}

# Define the endpoint for handling file extraction
@app.post("/extract_from_doc")
async def extract_from_doc(
        file_format: str = Form(...),
        file: UploadFile = File(...),
):
    # Read the contents of the uploaded file
    contents = await file.read()

    # Generate a unique file name and save the uploaded file
    file_name = str(uuid.uuid4()) + ".pdf"
    file_path = os.path.join(uploads_dir, file_name)

    with open(file_path, "wb") as f:
        f.write(contents)

    try:
    # Call the extraction function with the uploaded file and format
        data = extract(file_path, file_format)
    except Exception as e:
        # Handle any exceptions raised during extraction
        data = {'error': str(e)}

    # Remove the uploaded file after extraction
    if os.path.exists(file_path):
        os.remove(file_path)

    # Return the extracted data or an error message
    return data


# Run the FastAPI app using Uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
