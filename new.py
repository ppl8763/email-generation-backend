from google import genai
from PIL import Image
from io import BytesIO

client = genai.Client(api_key="AIzaSyCN8jPJwJARRbHCzCFHHY-qsoWBsvMFiUY")

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="A futuristic library with floating books and neon lighting, 4k resolution",
    config={'response_modalities': ['IMAGE']}
)

# Saving the generated image
for part in response.candidates[0].content.parts:
    if part.inline_data:
        img = Image.open(BytesIO(part.inline_data.data))
        img.save("generated_output.png")