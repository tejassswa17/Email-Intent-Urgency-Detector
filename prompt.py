from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate
)
from parser import parser

f_inst = parser.get_format_instructions()

# Prompt Template
prompt_template = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(
        template='''
You are an Email Intent & Urgency Detector.

Your task is to analyze the given email text and extract:
1. intent
2. urgency
3. tone

Rules:
- Strictly analyze only the provided input.
- Do not make assumptions.
- Do not use external context.
- Return output only in the specified JSON format.

Email Text:
{problem}

{format_instructions}
''',
        partial_variables={'format_instructions': f_inst}
    )
])