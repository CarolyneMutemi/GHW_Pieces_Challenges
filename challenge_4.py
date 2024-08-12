"""
Chatbot app with pieces.
"""
from pieces_copilot_sdk import PiecesClient
import streamlit as st

pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:5323'})
st.title('GHW Challenge 4: Pieces Copilot Chatbot')

with st.chat_message('assistant'):
    st.markdown("Hello, earthling! Here to reveal the universe's secrets. You just got to ask. :)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# # Display chat messages from history
# for message in st.session_state.messages:
#     with st.chat_message(message['role']):
#         st.markdown(message['content'])

# Accept user iput
if prompt := st.chat_input('Ask me anything!'):
    # Display user message in chat message container.
    with st.chat_message('user'):
        st.markdown(prompt)
    # Add user message to chat history.
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    # Create a conversation
    conversation_response = pieces_client.create_conversation(
    props={
        "name": "Test conversation",
        "firstMessage": prompt
    })

    if conversation_response:
        response = conversation_response['answer']['text']
        # Display response.
        with st.chat_message('assistant'):
            st.markdown(response)
        # Add response to history.
        st.session_state.messages.append({'role': 'assistant', 'content': response})
