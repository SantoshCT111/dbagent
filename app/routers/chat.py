from fastapi import APIRouter

from app.schemas.chat import ChatMessage
from app.services.ai_service import ai_brain
router = APIRouter(prefix="/chat",tags = ["chat"])


@router.post("/")
async def send_message(data: ChatMessage):

    text = data.text
    reply = await ai_brain.generate_response(text)

    return {"reply": reply}



