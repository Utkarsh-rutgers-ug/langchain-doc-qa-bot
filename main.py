import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Ollama chat
from langchain_openai import ChatOpenAI

st.title("📄 Document Q&A Bot (Ollama + Local FAISS)")

# 1) Upload
uploaded_file = st.file_uploader("Upload a text document", type=["txt"])
if not uploaded_file:
    st.info("Please upload a .txt file to begin.")
    st.stop()

# 2) Save & load
with open("uploaded_doc.txt", "wb") as f:
    f.write(uploaded_file.getbuffer())
loader = TextLoader("uploaded_doc.txt")
docs = loader.load()

# 3) Split
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 4) Embed locally with HuggingFace
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embeddings)

# 5) Use Ollama (make sure `ollama pull llama2` run previously)
llm = ChatOpenAI(
    model_name="mistral:latest",
    # openai_api_base="http://localhost:11434/v1",
    # openai_api_key="dummy_key",
)



# 6) Build QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 7) Chat interface
query = st.text_input("Ask a question about the document:")
if query:
    with st.spinner("Generating answer..."):
        answer = qa.run(query)
    st.success(answer)