from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


class AgentState(TypedDict):
    # 'messages' is a list. 
    # 'add_messages' is the reducer that appends new replies to the history.
    messages: Annotated[list, add_messages]



# 2. The Actor (Node) 🤖
async def call_model(state: AgentState):
    # We initialize the model inside the node or as a global
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
    
    # The AI looks at all the messages in the notebook
    response = await llm.ainvoke(state["messages"])
    
    # It writes its new answer into the notebook
    return {"messages": [response]}


async def review_node(state: AgentState):
    last_message = state["messages"][-1].content
    llm = ChatOpenAI(model="gpt-4o",temperature=0.5)

    response = await llm.ainvoke(state)
    

# 3. The Map (Graph) 🗺️
workflow = StateGraph(AgentState)

# Define our 'Thinking' room
workflow.add_node("chatbot", call_model)

# Set the path: Start -> Chatbot -> End
workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)

# Compile the "Mind"
compiled_graph = workflow.compile()




