from fastapi import FastAPI, HTTPException, Request, Body,File, UploadFile
from pydantic import BaseModel
from RAG.rag import RAG_chatbot
import shutil
import os

UPLOAD_DIR = "RAG/data"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure upload directory exists

bot = RAG_chatbot()
app = FastAPI()


class UserQuery(BaseModel):
    user_query: str

@app.get("/")
async def home(request: Request):
    return {"message": "Service running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save the file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "message": "File uploaded successfully"}
    

@app.post("/chat")
async def chat_endpoint(payload: UserQuery = Body(...)):
    try:
        response = await bot.get_response(payload.user_query)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# uvicorn app:app --reload