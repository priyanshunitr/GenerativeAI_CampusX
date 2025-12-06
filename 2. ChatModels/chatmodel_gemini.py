from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
# temperature - It is the parameter that control the randomness of a language model's output. It affects how creative or deterministic the responses are. (Lower - more deterministic, predictable. Higher - more random, creative, diverse) (0 to 2)

# max_completion_token - how many max token to get in output

result = model.invoke("What is the capital of India?")

print("Full result - ")
print(result)

print("\nResult Content - ")
print(result.content)