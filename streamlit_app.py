
import streamlit as st
from openai import OpenAI

# إعداد النموذج والعميل
client = OpenAI(api_key="PUT_YOUR_API_KEY_HERE")
model = "gpt-4o-mini"

st.title("Paris Tourist Chatbot 🌟")
st.write("Ask any question about Paris landmarks and tourist spots!")

user_input = st.text_input("Your question:")

if user_input:
    conversation = [
        {"role": "system", "content": "You are a helpful Travel Guide providing concise info about Paris landmarks."},
        {"role": "user", "content": user_input}
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=0.0,
        max_tokens=150
    )
    
    st.write("Assistant:", response.choices[0].message.content)
