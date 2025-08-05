# main.py

import streamlit as st
from tutor import (
    correct_grammar,
    get_vocabulary,
    start_conversation,
    chat_with_tutor,
    clear_conversation_memory
)

st.set_page_config(page_title="AI Language Tutor", layout="centered")
st.title("🧑‍🏫 AI Language Tutor")

option = st.sidebar.selectbox("Choose an activity", [
    "Grammar Correction",
    "Start a Conversation",
    "Vocabulary Builder"
])

# ----------------------------------
# Option 1: Grammar Correction
# ----------------------------------
if option == "Grammar Correction":
    st.markdown("### ✍️ Grammar Correction")
    user_input = st.text_area("Enter a sentence:")
    if st.button("Correct"):
        if user_input:
            response = correct_grammar(user_input)
            st.markdown("### ✅ Correction")
            st.write(response)
        else:
            st.warning("Please enter a sentence.")

# ----------------------------------
# Option 2: Two-Way Conversation
# ----------------------------------
elif option == "Start a Conversation":
    st.markdown("### 🗣️ Roleplay Conversation Practice")

    if "conversation_started" not in st.session_state:
        st.session_state.conversation_started = False
        st.session_state.messages = []

    # If not started yet
    if not st.session_state.conversation_started:
        language = st.selectbox("Choose a language", ["English", "Hindi", "Spanish"])
        role = st.text_input("Act as (e.g., waiter, teacher, friend)", value="waiter")

        if st.button("Start Roleplay"):
            starter = start_conversation(language, role)
            st.session_state.messages.append({"role": "assistant", "text": starter})
            st.session_state.conversation_started = True
            st.rerun()

    # Active conversation state
    else:
        st.info("You're now in a conversation. Reply below.")

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["text"])

        user_input = st.chat_input("Type your response...")
        if user_input:
            st.session_state.messages.append({"role": "user", "text": user_input})
            ai_response = chat_with_tutor(user_input)
            st.session_state.messages.append({"role": "assistant", "text": ai_response})
            st.rerun()

        # New conversation reset
        if st.button("🧹 Start New Conversation"):
            st.session_state.conversation_started = False
            st.session_state.messages = []
            clear_conversation_memory()
            st.rerun()

# ----------------------------------
# Option 3: Vocabulary Builder
# ----------------------------------
elif option == "Vocabulary Builder":
    st.markdown("### 📚 Daily Vocabulary")
    language = st.selectbox("Select a language", ["English", "Hindi", "Spanish"])
    if st.button("Get Vocabulary"):
        response = get_vocabulary(language)
        st.markdown("### ✅ Words")
        st.write(response)
