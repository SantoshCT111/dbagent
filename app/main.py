from fastapi import FastAPI
from pydantic import BaseModel,Field
import uvicorn

app = FastAPI()


class ChatMessage(BaseModel):
    text: str = Field(min_length=1, max_length=500)



@app.get("/")
def read_root():
    return {"status": "Agent Server is Live!"}


@app.post("/chat")
def chat(message: ChatMessage):
    # Here you would integrate your agent logic to process the message
    response = f"Echo: {message.text}"
    return {"response": response}




if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,        # The port to listen on
                reload=True
                )