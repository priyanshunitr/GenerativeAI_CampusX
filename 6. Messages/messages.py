from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

# there are 3 types of messages in Langchain
# 1. System Message - A system message (instruction - You are a helpful assistant...)
# 2. Human Message - user input
# 3. AI Message - response from AI

messsages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about LangChain")
]

result = model.invoke(messsages)
messsages.append(AIMessage(content=result.content))

print(messsages)
