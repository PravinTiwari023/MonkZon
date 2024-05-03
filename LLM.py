import os
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"),  model="llama3-70b-8192")

def generate_text(prompt):
    return llm.invoke([HumanMessage(content=prompt)]).content