import os
import sys
from dotenv import load_dotenv

from langchain.chat_models import AzureChatOpenAI

from langchain.prompts import PromptTemplate
from langchain.schema.messages import HumanMessage


this = sys.modules[__name__]
# load environment variables
load_dotenv()
# read environment variables
this.AZURE_OPENAI_EMBEDDING_MODEL_NAME = os.getenv("AZURE_OPENAI_EMBEDDING_MODEL_NAME")
this.AZURE_OPENAI_EMBEDDING_MODEL_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_EMBEDDING_MODEL_DEPLOYMENT_NAME")
this.AZURE_OPENAI_CHAT_MODEL_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_CHAT_MODEL_DEPLOYMENT_NAME")

def answer_the_question(question, isStreamed: bool = False):
    # prompt
    template ="You are helpful assistant, which can answer based off you knowledge.<question>{question}</question>"
    # setup prompt template
    prompt_template = PromptTemplate.from_template(template)

    # initialize LLM
    llm = AzureChatOpenAI(deployment_name=this.AZURE_OPENAI_CHAT_MODEL_DEPLOYMENT_NAME, temperature=0.5, streaming= isStreamed)
    
    while True:
        user_input = question
        if user_input.strip() == "":
            return 'Please ask a question'
        prompt = prompt_template.format(question=user_input)
        message = HumanMessage(content=prompt)
        if(isStreamed):
            result = llm.astream([message])
        else:
            result = llm([message])
        return result