import streamlit as st
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import HumanMessage, AIMessage

# Load .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

if not api_key:
    st.error("Groq API key not found.")
    st.info("Local: add to .env\nOnline: add in Streamlit Secrets")
    st.stop()

# Page config
st.set_page_config(page_title="Azundow Intelligent Document Chatbot", page_icon="🤖", layout="centered")

# Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("logo.png", width=100)
with col2:
    st.markdown("<h1 style='margin-top: 30px;'>Azundow Intelligent Document Chatbot</h1>", unsafe_allow_html=True)

st.caption("Built by Azundow — Ask questions on Python")

# Session state for messages and memory
if "messages" not in st.session_state:
    st.session_state.messages = []
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
if "chain" not in st.session_state:
    st.session_state.chain = None

# Load documents and build chain
if st.session_state.chain is None:
    docs = []
    folder = "documents"

    if os.path.exists(folder):
        files = [f for f in os.listdir(folder) if f.lower().endswith(('.pdf', '.csv'))]
        if files:
            for f in files:
                path = os.path.join(folder, f)
                try:
                    loader = PyPDFLoader(path) if f.lower().endswith(".pdf") else CSVLoader(path)
                    docs.extend(loader.load())
                except Exception as e:
                    st.warning(f"Could not load {f}: {e}")
        else:
            st.info("No documents in 'documents' folder → general mode")
    else:
        st.info("No 'documents' folder → general mode")

    if docs:
        with st.spinner("Building knowledge base…"):
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            splits = splitter.split_documents(docs)

            embeddings = HuggingFaceEmbeddings(
                model_name="all-MiniLM-L6-v2",
                model_kwargs={"device": "cpu"}
            )

            vector_store = Chroma(
                collection_name="azundow_collection",
                embedding_function=embeddings,
                persist_directory=None
            )
            vector_store.add_documents(splits)

            llm = ChatGroq(
                groq_api_key=api_key,
                model_name="llama-3.1-8b-instant",
                temperature=0.3
            )

            # Prompt with memory placeholder
            prompt = ChatPromptTemplate.from_messages([
                ("system", """You are a helpful Python tutor.
Use only the context below.
Answer in your own words.
Be clear, friendly and concise — keep responses short and to the point (maximum 250–300 words unless asked for detail).
Always try to include one or more short, practical Python code examples when helpful.
Context: {context}"""),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}")
            ])

            retriever = vector_store.as_retriever(search_kwargs={"k": 4})

            # Chain with memory
            chain = (
                {"context": retriever, "question": RunnablePassthrough(), "chat_history": st.session_state.memory.chat_memory}
                | prompt
                | llm
                | StrOutputParser()
            )

            st.session_state.chain = chain

        st.success("Documents loaded — ready!")
    else:
        st.info("No documents loaded — general Python help available")

# Chat interface
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            if st.session_state.chain:
                try:
                    # Invoke with memory
                    response = st.session_state.chain.invoke(prompt)
                    # Save to memory
                    st.session_state.memory.chat_memory.add_user_message(prompt)
                    st.session_state.memory.chat_memory.add_ai_message(response)
                except Exception as e:
                    response = f"Sorry — temporary error: {e}"
            else:
                response = "I can help with general Python questions!"
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.caption("Azundow Intelligent Document Chatbot — Fast • Professional")

















