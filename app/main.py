from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import uvicorn

from app.routers import chat

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app = FastAPI()

app.include_router(chat.router)

# Serve the chat UI at the root
@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    return (FRONTEND_DIR / "index.html").read_text()

# Serve any other static assets from frontend/
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")






if __name__ == "__main__":
    uvicorn.run("app.main:app",
                host="127.0.0.1",
                port=8000,        # The port to listen on
                reload=True
                )