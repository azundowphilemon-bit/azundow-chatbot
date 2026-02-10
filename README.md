# Azundow Intelligent Document Chatbot

**© 2025 Philemon Azundow. All rights reserved.**

This is a proprietary Python learning chatbot that features:
- **Personalized Learning**: Tracks your progress through Python tutorials.
- **Secure Authentication**: User login and registration backed by Google Sheets.
- **RAG Architecture**: Retrieves answers from local documents (PDFs, CSVs, W3Schools tutorials).

## Features
1.  **User Accounts**: Secure login/registration.
2.  **Progress Tracking**: Remembers your last studied topic.
3.  **Proactive Tutor**: Explains topics and suggests the next step in the curriculum.
4.  **Admin Ready**: Built on Streamlit and Google Cloud.

## Setup for Developers

### 1. Environment Variables
Create a `.streamlit/secrets.toml` file with your keys:
```toml
GROQ_API_KEY = "your-groq-key"

[gcp_service_account]
type = "service_account"
# ... your google cloud json key ...
```

### 2. Google Sheets
Create a Google Sheet named `azundow_users` with headers: `username`, `password`, `name`, `progress`.
Share it with your Service Account email.

### 3. Run Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---
**License**: Proprietary. You may not distribute or sell this software without permission.
Contact: **azundowphilemon@gmail.com**
