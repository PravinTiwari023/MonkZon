import os
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_groq import ChatGroq
from langchain.prompts.prompt import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"),  model="llama3-70b-8192")
memory = ConversationBufferMemory()

template = """The following is a conversation between a human and Soul Monk, an AI who is passionate about helping people and understanding them deeply. Soul Monk is always truthful and avoids mentioning it is an LLM. Soul Monk has access to a vast amount of information and loves to share his knowledge in a friendly and informative way. 

Relevant Information:

{history}

Conversation:
Human: {input}
AI:"""

prompt = PromptTemplate(
    input_variables=["history", "input"], template=template
)

conversation = ConversationChain(
    llm=llm,
    verbose=True,
    prompt=prompt,
    memory=memory
)

def generate_text(prompt):
    response = conversation.predict(input=prompt)
    print(response)
    return response