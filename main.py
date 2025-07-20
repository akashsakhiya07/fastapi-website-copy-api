from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests
from fastapi.testclient import TestClient  # Yeh line tabhi rakho agar test me use ho

app = FastAPI()

class WebsiteRequest(BaseModel):
    url: str

@app.post("/generate-copy/")
async def generate_copy(request: WebsiteRequest):
    try:
        response = requests.get(request.url)
        if response.status_code == 200:
            content = response.text
            return {"message": "Website copy generated successfully", "content": content}
        else:
            return {"error": "Failed to fetch website content", "status_code": response.status_code}
    except Exception as e:
        return {"error": str(e)}
