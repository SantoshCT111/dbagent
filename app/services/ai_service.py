class AIService:
    def __init__(self):
        self.model_name = "Gemini pro"

    async def generate_response(self,user_text : str) -> str:
        ai_reply = f"The ai pricesed : {user_text} and says : hello i am your budy" 
        return ai_reply
    


ai_brain = AIService()