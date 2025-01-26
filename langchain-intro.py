from langchain.chains.qa_generation.prompt import templ
from langchain.llms import OpenAI
from langchain_core.output_parsers import StrOutputParser
import os
import getpass
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

os.environ["OPENAI_API_KEY"]= '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'
print('Hello LangChain')

llm = OpenAI()
code_prompt = PromptTemplate(template='write a very {language} function that will complete {task}',input_variables=["language","task"])


code_chain = LLMChain(llm=llm,prompt = code_prompt)
lang = input('what\'s ur language')
task = input('whats ur task')
result = code_chain({
    "language":lang,
    "task":task
})
print(result["text"])


