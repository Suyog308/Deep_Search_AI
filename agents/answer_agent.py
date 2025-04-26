## deep-research-ai/agents/answer_agent.py

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

llm = ChatOpenAI(temperature=0.5)

prompt = ChatPromptTemplate.from_template(
    """
You are an expert answer drafter.
Using the following context:
{context}

Write a detailed answer to the user question:
{question}

Use a clear structure and cite the sources (if given).
    """
)

answer_chain = LLMChain(llm=llm, prompt=prompt)

def run_answer_agent(context, query):
    return answer_chain.run({"context": context, "question": query})