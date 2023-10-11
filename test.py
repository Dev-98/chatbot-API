from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

text = input("enter : ")

# print(messages[content])
try:
    # Load environment variables from .env file
    load_dotenv(find_dotenv())

    # Access the OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    print("api : ",api_key)

    llm = OpenAI(openai_api_key = api_key)

    feetful_of_fun_name = llm.predict_messages(text)[0]['content']
    
    print(feetful_of_fun_name)

except Exception as e:
    print(str(e))