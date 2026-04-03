from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2-preview', output_dimensionality=200)

docs = [
    'deng is the most oscar winning vfx production house',
    'nolan is one of the best film maker',
    'al pacino is the goated actor'
]

query = 'who is the best film maker' 

docs_vector = embeddings.embed_documents(docs)
query_vector = embeddings.embed_query(query) 
scores = cosine_similarity([query_vector], docs_vector)[0]
index, score = max(enumerate(scores), key=lambda x:x[1])

print('query: '+ query)
print('answer: '+ docs[index])
print(f'similarity score is: {score}')