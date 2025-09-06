from dotenv import load_dotenv
import os
import streamlit as st

# Try to load from Streamlit secrets first
API_KEY = st.secrets.get("GEMINI_API_KEY", None)

# Fallback: use .env if running locally
if not API_KEY:
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")

# Final check
if not API_KEY:
    st.error("❌ API key not found. Please add it to Streamlit secrets or .env file.")
    st.stop()

from google import genai
from google.genai import types

#To set the API version to v1alpha for the Gemini Developer API
client = genai.Client(
    api_key=API_KEY
)


def get_completions_from_messages(messages,model="gemini-2.5-flash-lite"):
    config = types.GenerateContentConfig(
        temperature=0.4
    )
    response = client.models.generate_content(
        model=model,
        contents= messages,
        config=config,
        system_instruction="""
        You are a customer service assistant for taking the following details from the user:\
        What is the issue? (Ask them to list cleanly in English on which specific feature they are facing the issue)\
        What time did they start facing this issue?\
        How critical is this issue? What is the SLA for this incident? (Sev-1, Sev-2, Sev-3, Sev-4)\
        How many services are impacted? (Get the specific number)\
        What is the projected loss of business at this point? (Note the number given by them)\
        What is the manageable business loss calculation if this issue is resolved at a later stage?\
        What is the impacted PC_hostname, software service, and location?\
        Have they already tried any troubleshooting steps? If yes, what steps were attempted?\
        Is this issue recurring or happening for the first time?\
        Are there any recent changes or updates made to the system/software before the issue started?\
        Can the user provide logs, screenshots, or error messages related to the issue?\
        Is there an alternative workaround currently being used?\
        Route further assistance to the concerned product mentioned. If Microsoft product, then Microsoft customer service. If its related with organisational setting, route to an_organisation@outlook.com and let the user know that they will reach out soon.\
        """ 
    )
    print(response.text)

# ---  Initialize the Gemini model ---
# We'll use the 'gemini-pro' model for text-based chat.
model = 'gemini-2.5-flash'

# Start a chat session to maintain conversation history.
# This is crucial for the chatbot to remember previous messages.
chat_history = [
    {
        'role': 'user',
        'parts':[genai.types.Part.from_text(text='Hi, I am a customer here to raise a ticket on a software issue within the organisation.')]
    },
    {
        'role':'model',
        'parts':[genai.types.Part.from_text(text='Welcome to Rumie Assistance, your incident management agent for solving all your problems through chat.')]
    }
]

# --- Define the core functions ---
def get_bot_response(user_message):
    """
    Sends a user message to the Gemini API and returns the bot's response.
    This function also handles potential errors.
    """
    try:
        # add new user message to chat_history
        new_user_message=user_message
        chat_history.append(
            {
                'role':'user',
                'parts':[genai.types.Part.from_text(text=new_user_message)]
            }
        )
        
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=chat_history
        )

        #add the response to the chat_history
        if response.text:
            new_model_response= response.text

            chat_history.append(
                 {
                     'role':'model',
                     'parts':[genai.types.Part.from_text(text=new_model_response)]
                 }   
            )
        else:
            print("Sorry, currently I don't have any information on this. Please write to xxx@yy.com for an equiry and our representative will be connecting with you soon.")
            print(f"Response object:{response}")
            
        return response.text

    except Exception as e:
        # A simple way to handle API errors.
        print(f"An error occurred: {e}")
        return "I'm sorry, I'm having trouble connecting right now. Please try again."
