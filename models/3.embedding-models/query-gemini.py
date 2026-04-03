from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2-preview', output_dimensionality=40)
vector = embeddings.embed_query("which is the best plant")
print(len(vector))