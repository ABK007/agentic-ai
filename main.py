from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import sys


llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key="AIzaSyDIrIP-uFh7gZzjV_PUvHwOG6SE1xzpLuc")

template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate.from_template(template)

chain = prompt | llm

question = "How much is 2+2?"

for chunk in llm.stream("Tell me a short poem about snow"):
    sys.stdout.write(chunk)
    sys.stdout.flush()
