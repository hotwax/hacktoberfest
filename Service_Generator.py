#install required liabraries
!pip install langchain
!pip install langchain-community 
!pip install langchain-community 

import os
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import google.generativeai as genai
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
os.environ["GEMINI_API_KEY"] = "AIzaSyDTtCaNmd-cXEy1dh6qcaCzNkl0moLfg0s"
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Load the documents (service guidelines, requirements, etc.)
loader = TextLoader('/content/service_generation_topic.pdf', encoding='latin-1') # Try different encodings like 'latin-1' or 'cp1252' if this doesn't work
documents = loader.load()

