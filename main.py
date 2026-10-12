import hashlib
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI Application Instance
app = FastAPI(title="Improvise Python App Activity")

# Task 1: Define the Pydantic Model structure for parsing payload text
class TextRequest(BaseModel):
    text: str

# Task 3: Add a customized Welcome Note with your name
@app.get("/")
async def root():
    """
    Root Endpoint returning a customized participant welcome note.
    """
    return {"message": "Welcome to the Python App! Participant: NAGESH THOTA"}

# Task 2 & 4: Create a POST endpoint that reads the text field and returns its MD5 checksum
@app.post("/generate")
async def generate_checksum(payload: TextRequest):
    """
    Accepts a POST request containing a JSON body with a single string 'text' key.
    Computes and returns a hexadecimal string digest of the text.
    """
    # Task 4 (Comments): Encode text to bytes for processing by hashlib
    text_bytes = payload.text.encode('utf-8')
    
    # Generate Hexadecimal MD5 Checksum
    generated_checksum = hashlib.md5(text_bytes).hexdigest()
    
    return {"checksum": generated_checksum}
