from fastapi import APIRouter
from model.schema import email
import google.generativeai as genai
import os 
router = APIRouter()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

@router.post("/email")
def send_email(data:email):
    prompt = f"""
You are an expert corporate communication specialist.

Generate a well-structured {data.tone} email.

Include:
1. Subject line
2. Proper greeting
3. Clear explanation of the purpose
4. Polite request or statement
5. Closing remark
6. Professional sign-off

Context:
Purpose: {data.purpose}
Recipient: {data.recipient_type}
Message: {data.message}
Sender: {data.sender_name}

Make sure:
- The tone matches the recipient type
- The language is natural and human-like
- No repetition
"""
    response = model.generate_content(prompt)
    return {
        "email":response.text
    }