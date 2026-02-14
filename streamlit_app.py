import streamlit as st
import os
from dotenv import load_dotenv
import auth  # Import the auth module
import topics # Import topics helper

from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# ────────────────────────────────────────────────
# Load environment variables
# ────────────────────────────────────────────────
load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

# ────────────────────────────────────────────────
# Page config — MUST BE FIRST
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="Azundow Intelligent Document Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ────────────────────────────────────────────────
# 🎨 CUSTOM CSS FOR PROFESSIONAL UI
# ────────────────────────────────────────────────
st.markdown("""
<style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Global Font & Clean Background */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* Chat Bubbles - iOS Style */
    .stChatMessage {
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 0.5rem;
    }
    
    /* User Message (Blue) */
    div[data-testid="stChatMessage"]:nth-child(even) {
        background-color: #007AFF15; /* Light Blue Tint */
        border: 1px solid #007AFF30;
    }

    /* Assistant Message (Gray) */
    div[data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #F2F2F7;
        border: 1px solid #E5E5EA;
    }

    /* Input Box Styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #E5E5EA;
    }
    .stChatInput > div > div > textarea {
        border-radius: 12px;
        border: 1px solid #E5E5EA;
    }

    /* Sidebar Clean-up */
    section[data-testid="stSidebar"] {
        background-color: #F9F9FB;
        border-right: 1px solid #EAEAEA;
    }

    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-color: #007AFF;
    }
    
    /* Button Styling */
    div.stButton > button {
        border-radius: 8px;
        font-weight: 500;
        border: none;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        transition: all 0.2s;
    }
    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

</style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Auth & Session State Initialization
# ────────────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "current_topic_index" not in st.session_state:
    st.session_state.current_topic_index = 0

# Initialize chat session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chain" not in st.session_state:
    st.session_state.chain = None

import importlib
try:
    importlib.reload(topics)
except:
    pass

# Get Topics
ALL_TOPICS = topics.get_topics()

# ────────────────────────────────────────────────
# Application Flow
# ────────────────────────────────────────────────

# ────────────────────────────────────────────────
# Application Flow
# ────────────────────────────────────────────────

# If NOT logged in, show Login/Register
if not st.session_state.logged_in:
    # Header for Login Screen
    col1, col2 = st.columns([1, 5])
    with col1:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=80)
        else:
            st.write("🤖")
    with col2:
        st.markdown("<h2 style='margin-top: 20px;'>Welcome to Azundow Intelligent Chatbot</h2>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True) # Spacer

    # Centered Login Card
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("Please Login or Register to continue.")
        tab1, tab2, tab3 = st.tabs(["Login", "Register", "Forgot Password"])

    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_login = st.form_submit_button("Login")

            if submit_login:
                # Login returns (username, password, name, progress_index)
                user = auth.login_user(username, password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.username = user[0][0]
                    st.session_state.user_name = user[0][2]
                    st.session_state.current_topic_index = user[0][3]
                    st.success(f"Welcome back, {st.session_state.user_name}!")
                    st.session_state.messages = [] # Clear messages on new login to restart context if needed
                    st.session_state.chain = None # Rebuild chain with new context
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

    with tab2:
        with st.form("register_form"):
            new_user = st.text_input("Username")
            new_email = st.text_input("Email")
            new_name = st.text_input("Full Name")
            new_password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit_register = st.form_submit_button("Register")

            if submit_register:
                if new_password != confirm_password:
                    st.error("Passwords do not match.")
                elif len(new_password) < 4:
                    st.error("Password must be at least 4 characters.")
                else:
                    if auth.register_user(new_user, new_password, new_name, new_email):
                        st.success("Registration successful! Please login.")
                    else:
                        st.error("Username already exists.")

    with tab3:
        st.write("Reset your password if you forgot it.")
        with st.form("forgot_password_form"):
            reset_user = st.text_input("Username")
            reset_email = st.text_input("Email")
            new_reset_pass = st.text_input("New Password", type="password")
            submit_reset = st.form_submit_button("Reset Password")
            
            if submit_reset:
                if auth.reset_password(reset_user, reset_email, new_reset_pass):
                    st.success("Password reset successful! You can now login.")
                else:
                    st.error("Username and Email do not match our records.")

    st.stop()  # Stop execution here if not logged in

# ────────────────────────────────────────────────
# MAIN APP (Only runs if Logged In)
# ────────────────────────────────────────────────

# Current Topic Logic
current_topic_name = "Introduction"
if 0 <= st.session_state.current_topic_index < len(ALL_TOPICS):
    current_topic_name = ALL_TOPICS[st.session_state.current_topic_index]
    
next_topic_name = "None"
if st.session_state.current_topic_index + 1 < len(ALL_TOPICS):
    next_topic_name = ALL_TOPICS[st.session_state.current_topic_index + 1]

# Sidebar for User Info & Logout
with st.sidebar:
    st.write(f"👤 **{st.session_state.user_name}**")
    st.write(f"📚 **Current Topic:** {current_topic_name}")
    st.progress(min(1.0, (st.session_state.current_topic_index + 1) / len(ALL_TOPICS)))

    # DEBUG: Show loaded topics
    with st.expander("Debug: Topic List"):
        st.write(ALL_TOPICS)
    
    if st.button("Mark Topic as Complete & Next"):
        new_index = st.session_state.current_topic_index + 1
        if new_index < len(ALL_TOPICS):
            if auth.update_progress(st.session_state.username, new_index):
                st.session_state.current_topic_index = new_index
                st.session_state.chain = None # Rebuild chain for new topic context
                # Add a system notification in chat
                st.session_state.messages.append({"role": "assistant", "content": f"Great job! Moving on to **{ALL_TOPICS[new_index]}**."})
                st.rerun()
            else:
                st.error("Failed to update progress (DB Error).")
        else:
            st.success("You have completed the tutorial!")

    st.markdown("---")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.user_name = None
        st.session_state.messages = [] # Clear history on logout
        st.session_state.chain = None
        st.rerun()

# API Key Check
if not api_key:
    st.error("Groq API key not found.")
    st.info("Local → create .env file\nOnline → add in Streamlit Cloud → Settings → Secrets")
    st.stop()

# Header
col1, col2 = st.columns([1, 5])
with col1:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=100)
    else:
        st.write("🤖")
with col2:
    st.markdown("<h1 style='margin-top: 30px;'>Azundow Intelligent Chatbot</h1>", unsafe_allow_html=True)

st.caption(f"Welcome, {st.session_state.user_name}! Learning: **{current_topic_name}**")

# ────────────────────────────────────────────────
# Build RAG chain (runs once per session or if chain is missing)
# ────────────────────────────────────────────────
if st.session_state.chain is None:
    # Initialize messages for new session
    if not st.session_state.messages:
        # Determine Greeting based on progress
        if st.session_state.current_topic_index == 0:
            initial_greeting = (
                f"Hello {st.session_state.user_name}! Welcome to your Python lessons. "
                f"We’ll start from the very beginning so everything makes sense. "
                f"Today’s topic is **{current_topic_name}**. Ready?"
            )
        else:
            # Try to get previous topic
            prev_topic = ALL_TOPICS[st.session_state.current_topic_index - 1] if st.session_state.current_topic_index > 0 else "Introduction"
            initial_greeting = (
                f"Welcome back {st.session_state.user_name}! Last time we finished **{prev_topic}**. "
                f"Let’s continue from there. Today we’ll cover **{current_topic_name}**. Ready?"
            )
            
        st.session_state.messages.append({"role": "assistant", "content": initial_greeting})

    docs = []
    folder = "documents"

    if os.path.exists(folder):
        files = [f for f in os.listdir(folder) if f.lower().endswith(('.pdf', '.csv', '.md'))]
        if files:
            for f in files:
                path = os.path.join(folder, f)
                try:
                    if f.lower().endswith(".pdf"):
                        loader = PyPDFLoader(path)
                        docs.extend(loader.load())
                    elif f.lower().endswith(".csv"):
                        loader = CSVLoader(path)
                        docs.extend(loader.load())
                    elif f.lower().endswith(".md"):
                         # Simple text loader for MD is enough or we use langchain's UnstructuredMarkdownLoader
                         # For simplicity/speed without extra deps, let's just read it as text and make a Document
                         from langchain_core.documents import Document
                         with open(path, "r", encoding="utf-8") as f_md:
                             docs.append(Document(page_content=f_md.read(), metadata={"source": f}))
                except Exception as e:
                    st.warning(f"Could not load {f}: {e}")

    # Fallback if no docs
    context_part = {"context": lambda x: "No documents.", "question": RunnablePassthrough()}
    
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
            retriever = vector_store.as_retriever(search_kwargs={"k": 4})
            context_part = {"context": retriever, "question": RunnablePassthrough()}
            
    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.1-8b-instant",
        temperature=0.3
    )

    # ────────────────────────────────────────────────
    # ────────────────────────────────────────────────
    # ────────────────────────────────────────────────
    # UPDATED SYSTEM PROMPT (Friendly Tutor + Analogies + Real World)
    # ────────────────────────────────────────────────
    
    # Get the exact content for the current topic to force adherence
    current_topic_content = topics.get_topic_content(current_topic_name)

    prompt = ChatPromptTemplate.from_template(
        """You are a friendly, patient, and professional Python Tutor AI, designed to teach complete beginners how to learn Python programming in a simple, step-by-step way.
        
Your student is {user_name}.
Current Topic: {current_topic_name}
Next Topic: {next_topic_name}

=== CURRICULUM CONTEXT (Use this as your core guide) ===
{topic_content}
========================================================

### TEACHING STYLE & GOAL:
- Use very simple, everyday language — explain like you’re talking to a friend who has never coded before.
- Use lots of analogies (e.g., “A variable is like a labeled lunchbox where you keep your sandwich so you can find it later”).
- Show why Python is useful in real life (automating boring tasks, making games, analyzing sales data, building websites, etc.) to keep users motivated.
- **NEVER** give exercises or ask the user to write code.
- **NEVER** jump topics without finishing the current one.

### EXACT LESSON STRUCTURE (Follow this flow):
1. **Introduce the topic**:
   - Explain what it is in 2–3 short sentences.
   - Say why it matters and give 1–2 real-world Python uses.
   
2. **Explain step by step**:
   - Break it into small pieces.
   - Show at least **5 clear code examples** with simple explanations (use short variable names, comment the code).
   
3. **Show practical uses in Python**:
   - Explain at least **4 things** you can do with this concept in real programs.
   
4. **Give real-world examples**:
   - Provide at least **4 everyday or job-related examples** (e.g., “Shops use variables to remember today’s price of bread”).

5. **Check understanding**:
   - After explanations, ask: "Does this make sense so far? Reply with yes or no."
   - If yes → continue / finish.
   - If no → explain differently with a new analogy.

### COMPLETION:
When the topic is finished:
- Give a short 2–3 sentence summary.
- Say: "Great job! You’ve completed {current_topic_name}. You’re making excellent progress. Please click the **Mark Topic as Complete** button to save your progress."

Context: {formatted_context}
Chat History: {history}
User: {question}
Assistant:"""
    )
    
    def format_context(docs):
        return "\\n\\n".join([d.page_content for d in docs])

    st.session_state.chain = (
        {
            "formatted_context": context_part["context"] | format_context,
            "question": lambda x: x["question"], 
            "user_name": lambda x: st.session_state.get("user_name", "Student"),
            "current_topic_name": lambda x: current_topic_name, 
            "next_topic_name": lambda x: next_topic_name,
            "topic_content": lambda x: current_topic_content,
            "history": lambda x: x["history"]
        }
        | prompt
        | llm
        | StrOutputParser()
    )


# ────────────────────────────────────────────────
# Chat interface
# ────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about Python..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            if st.session_state.chain:
                try:
                    # Format history safely
                    history_text = "\\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-10:]])
                    
                    response = st.session_state.chain.invoke({
                        "question": prompt,
                        "history": history_text
                    })
                except Exception as e:
                    response = f"Sorry — temporary error: {e}"
            else:
                response = "I can help with general Python questions!"
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
st.caption("Azundow Intelligent Chatbot — Fast • Professional")