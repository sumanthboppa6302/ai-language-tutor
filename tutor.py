# tutor.py

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from prompts import grammar_correction_prompt, conversation_prompt, vocab_prompt

# Load API keys from secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]
base_url = st.secrets["TOGETHER_BASE_URL"]

# Initialize model
llm = ChatOpenAI(
    temperature=0.5,
    model="mistralai/Mistral-7B-Instruct-v0.2",
    openai_api_key=openai_api_key,
    openai_api_base=base_url
)

# Memory for conversation chain
memory = ConversationBufferMemory()
conversation_chain = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

def correct_grammar(sentence: str) -> str:
    prompt = PromptTemplate.from_template(grammar_correction_prompt)
    return llm.predict(prompt.format(sentence=sentence))

def start_conversation(language: str, role: str) -> str:
    prompt = PromptTemplate.from_template(conversation_prompt)
    return llm.predict(prompt.format(language=language, role=role))

def get_vocabulary(language: str) -> str:
    prompt = PromptTemplate.from_template(vocab_prompt)
    return llm.predict(prompt.format(language=language))

def chat_with_tutor(user_input: str) -> str:
    return conversation_chain.run(user_input)

def clear_conversation_memory():
    """Clears conversation memory."""
    global memory, conversation_chain
    memory.clear()
    memory = ConversationBufferMemory()
    conversation_chain.memory = memory
