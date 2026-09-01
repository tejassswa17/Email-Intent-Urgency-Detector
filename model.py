from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompt import prompt_template
from parser import parser

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

chain = prompt_template | llm | parser
