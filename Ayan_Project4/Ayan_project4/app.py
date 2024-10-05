# %%writefile app.py
import streamlit as st
import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def parse_request(request_text):
    doc = nlp(request_text)
    action, entity = None, None
    for token in doc:
        if token.dep_ == "ROOT":
            action = token.lemma_  # Main verb
        if token.pos_ == "NOUN":
            entity = token.text  # Extract noun as entity
    return action, entity

def generate_flask_service(entity_name, action):
    code = f"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/{entity_name}', methods=['POST'])
def {action}_{entity_name}():
    data = request.get_json()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
"""
    return code

# Streamlit app interface
st.title("AI-Powered Service Generator")

request_text = st.text_input("Enter your service request (e.g., 'Create a service to add an order'): ")

if st.button("Generate Service Code"):
    action, entity = parse_request(request_text)
    if action and entity:
        service_code = generate_flask_service(entity, action)
        st.code(service_code, language='python')
    else:
        st.error("Could not parse the request. Please try again.")
