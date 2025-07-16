# langchain-doc-qa-bot


## Overview

**langchain-doc-qa-bot** is a powerful, user-friendly application that allows users to upload any plain text document and interactively ask questions about its content. Built with cutting-edge technologies—LangChain for orchestration, FAISS for vector storage, HuggingFace or Ollama for local inference, and Streamlit for a sleek web interface—this project showcases your ability to integrate multiple AI/ML tools into a cohesive product.

**Key Highlights for Recruiters & Companies:**
- **End-to-End Pipeline:** Document ingestion, chunking, embedding, vector storage, retrieval, and response generation.  
- **Cloud & Local Flexibility:** Out-of-the-box support for local FAISS or Pinecone as a vector database, and local or cloud LLMs (OpenAI, Ollama, HuggingFace).  
- **Scalable Architecture:** Easily swap embeddings and vector stores to suit performance and budget.  
- **Professional UI/UX:** Streamlit-based front-end with Markdown + LaTeX rendering for technical content.

---

## Features

- **File Upload:** Seamlessly upload `.txt` documents via drag-and-drop.  
- **Document Chunking:** Automatic text splitting with overlap to optimize for LLM token limits.  
- **Embeddings:** Choose between OpenAI, HuggingFace, or any custom embedding model.  
- **Vector Storage:** In-memory FAISS for development, or Pinecone for production-grade scaling.  
- **Retrieval & QA:** LangChain `RetrievalQA` chain to fetch relevant context and generate concise, accurate answers.  
- **Rich Formatting:** Markdown + LaTeX support for mathematical expressions.

---

## Why It Matters

In today’s data-driven world, extracting actionable insights from large documents is crucial. This bot illustrates:

- **Rapid Prototyping:** Assemble complex AI workflows in minutes using LangChain.  
- **Practical ML Ops:** Manage embeddings, vector DBs, and LLM endpoints in one codebase.  
- **User-Centric Design:** Intuitive web interface lowers the barrier for non-technical users.

---

## Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/langchain-doc-qa-bot.git
   cd langchain-doc-qa-bot
2. **Create a .env
   ```bash
   cp .env.example .env
    # Then edit .env with your keys:
    # OPENAI_API_KEY=sk-your-openai-key (if you have one)
    # OPENAI_API_BASE=http://localhost:11434/v1   # for Ollama only
3. **Install dependencies
   ```bash
   pip install -r requirements.txt
4. **(Optional) Pull Ollama model
   ```bash
   ollama pull mistral:latest  # or llama2, vicuna, etc.
5. **Run the app
   ```bash
   streamlit run maincode.py
6. **Open http://localhost:8501 in your browser.

---

## Architecture Diagram

1. User Uploads Document
2. TextLoader ingests and CharacterTextSplitter chunks it.
3. Embeddings generate vectors (OpenAI / HuggingFace).
4. VectorStore persists in FAISS or Pinecone.
5. RetrievalQA fetches top-k context, then ChatOpenAI/Ollama generates answer.
6. Streamlit UI renders Markdown + LaTeX for polished output.

___

## Usage Examples:

Upload a PDF-exported text and ask:
- “What is the power rule in calculus?”

Provide a research paper and query:
- “Summarize the methodology section.”

Chat about your own notes:
- “List the key takeaways from section 2.”

___

## Repository Structure

├── main.py              # Streamlit app entrypoint
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── exapletxtfile.txt    # Example text file to put in the bot
├── README.md            # This file

___

## License

Distributed under the MIT License.


