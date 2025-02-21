import streamlit as st
import requests
import json

def get_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-small-24b-instruct-2501",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        try:
            return response.json()["choices"][0]["message"]["content"]
        except (KeyError, IndexError):
            return "Unexpected response format. Please check the API response."
    else:
        return f"Error: {response.status_code}\n{response.text}"

# Streamlit UI
st.title("Ethical Thinker")
st.write("What's your problem?")

prompt = st.text_area("Enter here...", "here...")

if st.button("Give solution"):
    with st.spinner("Wait a min...."):
        response_text = get_response(prompt)
    st.text_area("Response:", response_text, height=200)
