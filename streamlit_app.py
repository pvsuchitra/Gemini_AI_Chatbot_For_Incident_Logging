
import time
import numpy as np
import pandas as pd
import streamlit as st
from gemini_chat_bot import get_bot_response
import os

def stream_data(anyString):
    for word in anyString.split(" "):
        yield word + " "
        time.sleep(0.02)

#prevent any watchdog warnings when running on Streamlit cloud
os.environ["STREAMLIT_DISABLE_WATCHDOG_WARNING"] = "true"

# Get the bot's response and print it.
#bot_response = get_bot_response(prompt)
#with st.chat_message("assistant"):
#    response = st.write_stream(stream_data(bot_response))

def main():
    """
    This is the main function that runs the chatbot.
    It prints a welcome message and then enters a loop to get user input.
    """
    st.title("👩‍💻 :orange[Rumie] Assistant",anchor='RumieAssistant',help=None)
    st.subheader("Welcome! This is Rumie, your assistant to all your software problems.",divider=True)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history an app rerun
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message["content"])
        
    if prompt := st.chat_input("Hi! How may I assist you?"):
        #chat_input strips all the new lines and converts to single string, so we add them to display exact structure prompted from user.
        prompt = prompt.replace("\n", "  \n")
        with st.chat_message("user"):
            st.write(prompt)
        #add user message to chat history
        st.session_state.messages.append({'role':'user',"content":prompt})
        
        # Get the bot's response and print it.
        bot_response = get_bot_response(prompt)
        #print(f"Chatbot: {bot_response}")
        with st.chat_message("assistant"):
            st.write_stream(stream_data(bot_response))
        
        st.session_state.messages.append({'role':'model','content':bot_response})
            

# --- Step 5: Run the chatbot ---
if __name__ == "__main__":
    main()