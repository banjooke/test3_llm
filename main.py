import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

openai_api_key = st.secrets["openai"]["OPENAI_API_KEY"]

llm = OpenAI(api_key=openai_api_key)
template = "You are an experienced scientist and you write scientific blog {topic} only"
prompt = PromptTemplate(template=template, input_variables = ["topic"] )
llm_chain=LLMChain(prompt=prompt, llm=llm)

st.title("Scientific Blog App with LangChain")
user_topic = st.text_input("WHich topic do you want to write about?")

if st.button("Generate Contents"):
    if user_topic:
        response = llm_chain.run(topic=user_topic, max_tokens=2000)
        st.write(response)
    else:
        st.write("Please enter a topic")

