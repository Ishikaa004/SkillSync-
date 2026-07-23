from fastapi import FastAPI
from api.upload import router as upload_router

# Create the FastAPI application
app = FastAPI(
    title="SkillSync",
    version="1.0.0"
)

app.include_router(upload_router)

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to SkillSync API!"
    }