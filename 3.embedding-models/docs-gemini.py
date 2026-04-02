from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2-preview', output_dimensionality=40)

docs = [
    'who is the best cricketer',
    'who is the best football player',
    'who is the best basket player',
]

vector = embeddings.embed_documents(docs)
print(str(vector))