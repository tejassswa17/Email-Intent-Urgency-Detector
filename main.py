from parser import InputFormat
from prompt import prompt_template
from model import llm
from parser import parser

chain = prompt_template | llm | parser

problem = input("Enter Email Text: ")

# Validate input
validated_input = InputFormat(problem=problem)

response = chain.invoke({
    "problem": validated_input.problem
})

print(response.model_dump_json(indent=2))