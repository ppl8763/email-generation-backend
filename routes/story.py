from fastapi import APIRouter
from model.schema import new
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
router = APIRouter()

genai.configure(api_key="AIzaSyAcFxZHkBTAWvDu9XD00W_lDGsEWKkRyys")
model = genai.GenerativeModel("gemini-2.5-flash")

@router.post("/prompt")
async def showing(data:new):
    prompt=f"""
    You are a professional creative writer.

    Write a {data.about} story based on the topic:
    "{data.title}"

    Requirements:
    - Include:
        1. Title
        2. Main character
        3. Strong emotional buildup
        4. Twist ending
    - Make it engaging and descriptive.
    """
    response = model.generate_content(prompt)

    return {
        "topic":data.title,
        "about":data.about,
        "story":response.text
    }