from app.agent.graph import compiled_graph
class AIService:
    def __init__(self):
        self.agent = compiled_graph  # This is the compiled graph from graph.py

    async def generate_response(self,user_text : str) -> str:
        inputs = {"messages": [("user", user_text)]}
        result = await self.agent.ainvoke(inputs)


        # The result will be a dictionary with the new messages

        return result["messages"][-1].content   # Get the last message's text (the AI's reply)
    


ai_brain = AIService()