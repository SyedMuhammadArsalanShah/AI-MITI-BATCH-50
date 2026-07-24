from google import genai
import streamlit as st

st.title("Chat BOT MITI")

userPrompt=st.text_input("Enter Your Prompt here")


client = genai.Client(api_key="Your API key Here ")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=userPrompt
)

st.markdown(interaction.output_text)
