from fastapi import FastAPI
from routes.story import router as story_router
from routes.email import router as email_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://email-generation-backend-2.onrender.com"],  # ✅ no trailing slash
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story_router)
app.include_router(email_router)

@app.get("/")
def root():
    return {"message": "Hello"}