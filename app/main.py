from fastapi import FastAPI
from pydantic import BaseModel,Field
import uvicorn

app = FastAPI()








if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,        # The port to listen on
                reload=True
                )