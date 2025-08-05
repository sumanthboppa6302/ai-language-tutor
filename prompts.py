# prompts.py

grammar_correction_prompt = """
You are a helpful language tutor. A user has written the following sentence:
"{sentence}"

Correct the sentence and explain the correction.
"""

conversation_prompt = """
You are simulating a conversation for someone learning {language}.
Act like a {role}, and keep the conversation simple and friendly.
Start the conversation now.
"""

vocab_prompt = """
Give me 5 commonly used words in {language} with meanings and example sentences.
"""
