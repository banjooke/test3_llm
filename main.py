import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from langchain_core.prompts import ChatPromptTemplate

openai_api_key = st.secrets["openai"]["OPENAI_API_KEY"]

llm = OpenAI(api_key=openai_api_key)
template = ChatPromptTemplate.from_message (
    [
       (
           "system", "You are a Chemistry Teacher, you only address chemistry related questions"
       ) ,
        (
            "user","{topic}"
        )
    ]
)
prompt = template.format_messages(input_variables = ["topic"] )


st.title("Scientific Blog App with LangChain")
user_topic = st.text_input("WHich topic do you want to write about?")

if st.button("Generate Contents"):
    if user_topic:
        response = llm.invoke(prompt, max_tokens=2000)
        st.write(response)
    else:
        st.write("Please enter a topic")

