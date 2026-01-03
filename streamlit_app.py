import streamlit as st
import os
from dotenv import load_dotenv

# Critical fix for Streamlit Cloud sqlite3
try:
    import pysqlite3 as sqlite3
    import sys
    sys.modules["sqlite3"] = sqlite3
except ImportError:
    pass

import chromadb
from chromadb.config import Settings
from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load secrets
load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
if not api_key:
    st.error("Groq API key not found. Add it in Secrets (Cloud) or .env (local).")
    st.stop()

# Page setup
st.set_page_config(
    page_title="Azundow Intelligent Document Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("logo.png", width=100)
with col2:
    st.markdown("<h1 style='margin-top: 30px;'>Azundow Intelligent Document Chatbot</h1>", unsafe_allow_html=True)

st.caption("Built by Azundow — Ask questions on Python")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chain" not in st.session_state:
    st.session_state.chain = None
if "docs_loaded" not in st.session_state:
    st.session_state.docs_loaded = False

# Safe folder for the knowledge base
persist_dir = "./chroma_db"
os.makedirs(persist_dir, exist_ok=True)

@st.cache_resource(show_spinner="Loading documents and building knowledge base...")
def build_rag_chain(_api_key):
    documents_folder = "documents"
    docs = []

    # Load PDFs and CSVs
    if os.path.exists(documents_folder):
        files = [f for f in os.listdir(documents_folder) if f.lower().endswith(('.pdf', '.csv'))]
        if not files:
            return None, "No documents found → general Python chat mode"
        for filename in files:
            file_path = os.path.join(documents_folder, filename)
            ext = filename.lower().split(".")[-1]
            loader = PyPDFLoader(file_path) if ext == "pdf" else CSVLoader(file_path)
            docs.extend(loader.load())
    else:
        return None, "No 'documents' folder → general Python help mode"

    if not docs:
        return None, "No content loaded → general mode"

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    # === PERMANENT FIX FOR NEW CHROMA (2026) ===
    settings = Settings(anonymized_telemetry=False)

    # Create tenant and database if they don't exist (only runs once)
    admin_client = chromadb.AdminClient(settings=settings)
    try:
        admin_client.create_tenant(name="default_tenant")
    except:
        pass  # already exists
    try:
        admin_client.create_database(name="default_database", tenant="default_tenant")
    except:
        pass  # already exists

    # Normal persistent client
    chroma_client = chromadb.PersistentClient(
        path=persist_dir,
        settings=settings,
        tenant="default_tenant",
        database="default_database"
    )
    # === END OF FIX ===

    # Connect to collection
    vector_store = Chroma(
        client=chroma_client,
        collection_name="azundow_collection",
        embedding_function=embeddings,
    )

    # Index documents only the very first time
    if vector_store._collection.count() == 0:
        with st.spinner("Indexing your documents... (this happens only once









