from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Endpoints
@app.get("/ping")
async def ping():
    return {"message": "pong"}
