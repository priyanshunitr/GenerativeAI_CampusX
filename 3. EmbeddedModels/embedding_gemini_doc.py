from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

documents = [
    "Delhi is the capital of India",
    "Mumbai is capital of Maharashtra"
    "Paris is capital of France"
]

result = embedding_model.embed_documents(documents)

print(str(result))