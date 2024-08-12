"""
Coding Challenge 3
--------------------
Build a “Hello World” App Using Pieces Copilot SDK

Objectives:
1. Create a simple “Hello World” application utilizing
the Pieces Copilot SDK in either Typescript or Python.
2. Integrate the functionality to ask a predefined question to the
language model (LLM) using the “askQuestion” method and print the generated response.
"""
from pieces_copilot_sdk import PiecesClient
import streamlit as st

pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:5323'})

st.title('Pieces GHW: Coding Challenge 3')

question = "What are websockets?"
st.write(question)

response = pieces_client.ask_question(question)
st.write(response)
