from langchain.chains.qa_generation.prompt import templ
from langchain.llms import OpenAI
from langchain_core.output_parsers import StrOutputParser
import os
import getpass
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import  SequentialChain

os.environ["OPENAI_API_KEY"]= ''
print('Hello LangChain')

llm = OpenAI()
code_prompt = PromptTemplate(template='write a very {language} function that will complete {task}',input_variables=["language","task"])

test_prompt = PromptTemplate(template='write a test using Pytest {language} for {code}',input_variables=["language","code"])

code_chain = LLMChain(llm=llm,prompt = code_prompt,output_key="code")
test_chain = LLMChain(llm=llm,prompt=test_prompt,output_key = "test")
lang = input('what\'s ur language')
task = input('whats ur task')

chain = SequentialChain(
    chains=[code_chain,test_chain],
    input_variables = ["language","task"],
    output_variables = ["test","code"]
)
result = chain({
    "language":lang,
    "task":task
})
print(result['test'])


