import streamlit as st
from google.cloud import aiplatform
from google.auth import default
import os

# === YOUR PROJECT DETAILS ===
PROJECT_ID = "azundow-rag-assistant"          # your project ID
LOCATION = "global"                           # usually "global"
AGENT_DISPLAY_NAME = "azundow-rag-assistant"  # exact agent name from Agent Builder

# Page config
st.set_page_config(page_title="Azundow Vertex AI Chatbot", page_icon="🤖", layout="centered")

# Title with logo
col1, col2 = st.columns([1, 5])
with col1:
    st.image("logo.png", width=100)
with col2:
    st.markdown("<h1 style='margin-top: 30px;'>Azundow Vertex AI Chatbot</h1>", unsafe_allow_html=True)

st.caption("Powered by Google Vertex AI • Built by Azundow")

# Initialize Vertex AI
try:
    credentials, _ = default()
    aiplatform.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)
    st.success("Connected to Vertex AI")
except Exception as e:
    st.error(f"Connection failed: {e}")
    st.info("Run: `gcloud auth application-default login --scopes=https://www.googleapis.com/auth/cloud-platform`")
    st.stop()

# Find your agent endpoint
with st.spinner("Connecting to your agent..."):
    try:
        endpoints = aiplatform.Endpoint.list(
            filter=f"display_name={AGENT_DISPLAY_NAME}"
        )
        if not endpoints:
            st.error(f"Agent '{AGENT_DISPLAY_NAME}' not found. Check the name in Agent Builder.")
            st.stop()
        endpoint = endpoints[0]
        st.success(f"Agent '{AGENT_DISPLAY_NAME}' is ready!")
    except Exception as e:
        st.error(f"Agent lookup failed: {e}")
        st.stop()

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about your documents or Python..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching with Gemini..."):
            try:
                response = endpoint.predict(instances=[{"content": prompt}])
                predictions = response.predictions
                if not predictions or "content" not in predictions[0]:
                    answer = "The agent did not return any content."
                    citations = []
                else:
                    answer = predictions[0].get("content", "No content returned.")
                    citations = predictions[0].get("citationMetadata", {}).get("citations", [])

                st.markdown(answer)

                # Show sources if available
                if citations:
                    st.markdown("**Sources:**")
                    for c in citations:
                        title = c.get("title", "Document")
                        page = c.get("startIndex", "")
                        st.markdown(f"- {title} (page {page})")

            except Exception as e:
                answer = f"Error: {e}"
                st.error(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown("---")
st.caption("Azundow Intelligent Document Chatbot — Vertex AI RAG • Professional")
