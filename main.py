from fastapi import FastAPI
from routes.story import router as get
from routes.email import router as email
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(get)
app.include_router(email)
@app.get("/")
def get():
    return { "message":"Hello"}

