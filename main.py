from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient
import random

app = FastAPI()

class CopyInput(BaseModel):
    service: str
    audience: str
    tone: str

@app.post("/generate_copy")
def generate_copy(data: CopyInput):
    headlines = [f"Level Up Your {data.service} Game With Confidence"]
    ctas = ["Get your free copy preview now!", "See it in action", "Get started now"]
    features = [
        f"{data.service} tailored for {data.audience}",
        "High-converting and SEO-friendly content",
        "Delivered fast, with zero hassle",
        "Clear communication & revisions included"
    ]
    about = f"We specialize in {data.service} that helps {data.audience} stand out online. Our process is simple, fast, and focused on results."

    return {
        "headline": random.choice(headlines),
        "hero_section": f"We make {data.service} simple, powerful, and results-driven — all tailored for {data.audience}.",
        "features": features,
        "cta": random.choice(ctas),
        "about": about
    }

# # Test block
# client = TestClient(app)

# sample_input = {
#     "service": "Website Copywriting",
#     "audience": "SaaS Startup Founders",
#     "tone": "Professional"
# }

# response = client.post("/generate_copy", json=sample_input)
# print(response.status_code)
# print(response.json())
