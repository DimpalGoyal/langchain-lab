import streamlit as st
from langchain_core.prompts import PromptTemplate 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt_input = st.selectbox('select the question', ["what does the return funciton do in python","what is callback function in javascript"])

length_input = st.selectbox('select answer length', ["short(2-3 paragraph)","long(6-7 paragraph)"])

template = PromptTemplate(
    template="""
    you are a coding expert and your work is to answer coding related questions.
    explain the coding question: {prompt_input}
    explaination length: {length_input}
    1. Coding details:
      - include relavent coding snippets
      - explain the coding snippets with real life examples
""",
input_variables=['prompt_input', 'length_input']
)

prompt = template.invoke({
    'prompt_input': prompt_input,
    'length_input': length_input
})

if st.button('generate'):
    result = model.invoke(prompt)
    st.write(result.content)