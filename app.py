from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Initialize the app
app = FastAPI(title="BaseRead API")

# Allow your HTML frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local testing
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/upload")
async def process_vcf(file: UploadFile = File(...)):
    """
    Endpoint to receive the uploaded VCF file from the frontend.
    """
    # Read the contents of the uploaded file
    contents = await file.read()
    file_size = len(contents)
    
    # FUTURE: We will add the cyvcf2 parsing logic here!
    
    return {
        "status": "success",
        "filename": file.filename,
        "size_bytes": file_size,
        "message": f"Successfully received {file.filename}. Ready to parse variants!"
    }

if __name__ == "__main__":
    # Runs the server locally on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)