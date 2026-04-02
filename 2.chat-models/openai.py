from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="", temperature='', max_completion_tokens='')
result = model.invoke("prompt")
print(result)

