from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
# temperature - It is the parameter that control the randomness of a language model's output. It affects how creative or deterministic the responses are. (Lower - more deterministic, predictable. Higher - more random, creative, diverse) (0 to 2)
# If temp is 0, for same input everytime same output will be generated, whereas, for 1.5, everytime it will try to generate new output

# max_completion_token - how many max token to get in output

result = model.invoke("What is the capital of India?")

print("Full result - ")
print(result)

print("\nResult Content - ")
print(result.content)