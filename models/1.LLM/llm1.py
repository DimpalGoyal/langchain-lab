# old way to do things, chat models is the new way

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo')
result = llm.invoke("what is the capital of india")
print(result)
