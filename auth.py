import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import hashlib
import smtplib
import ssl
from email.message import EmailMessage
import random
import string

# Scope for Google Sheets and Drive
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

SHEET_NAME = "azundo_users"

def get_db_connection():
    """Establishes connection to Google Sheets."""
    try:
        if "gcp_service_account" not in st.secrets:
            return None, "Missing Google Cloud secrets. Please configure .streamlit/secrets.toml."
        
        # Load credentials from Streamlit secrets
        creds_dict = dict(st.secrets["gcp_service_account"])
        credentials = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
        client = gspread.authorize(credentials)
        
        # Open the spreadsheet
        sheet = client.open(SHEET_NAME).sheet1
        return sheet, None
    except FileNotFoundError:
        return None, "Secrets file not found. Please create .streamlit/secrets.toml."
    except Exception as e:
        return None, f"Connection Error: {e}"

def send_email(to_email, subject, body):
    """Sends an email using credentials from secrets."""
    try:
        if "email" not in st.secrets:
            return False, "Email secrets not configured."

        email_sender = st.secrets["email"]["address"]
        email_password = st.secrets["email"]["password"]
        smtp_server = st.secrets["email"]["smtp_server"]
        smtp_port = st.secrets["email"]["smtp_port"]
        
        if email_sender == "your-email@gmail.com":
             return False, "Email credentials are still default placeholders."

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = to_email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls(context=context)
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, to_email, em.as_string())
        return True, "Email sent successfully."
    except Exception as e:
        print(f"Email Error: {e}")
        return False, f"Failed to send email: {e}"

def init_db():
    """Checks if the database (Sheet) is accessible and set up."""
    sheet, error = get_db_connection()
    if error:
        st.error(f"Database Error: {error}")
        return False
    
    try:
        # Check if headers exist
        # Check if headers exist
        headers = sheet.row_values(1)
        expected_headers = ["username", "password", "name", "email", "progress"]
        
        if not headers:
            # Empty sheet, set headers
            sheet.append_row(expected_headers)
            sheet.update_cell(1, 6, "deleted") # Ensure deleted is there too if we just created it
        
        # Enforce Schema for existing sheets
        # Check Column 5 (Progress)
        val5 = sheet.cell(1, 5).value
        if val5 != "progress":
             print(f"DEBUG: Overwriting Col 5 '{val5}' with 'progress'")
             sheet.update_cell(1, 5, "progress")
             
        # Check Column 6 (Deleted)
        val6 = sheet.cell(1, 6).value
        if val6 != "deleted":
             sheet.update_cell(1, 6, "deleted")
             
        return True
    except Exception as e:
        st.error(f"Failed to initialize DB: {e}")
        return False

def make_hashes(password):
    """Hashes a password with SHA256."""
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    """Checks if a password matches the hash."""
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def register_user(username, password, name, email):
    """Registers a new user in Google Sheets."""
    sheet, error = get_db_connection()
    if not sheet:
        return False, "Database connection failed."

    try:
        # Check if username already exists
        records = sheet.get_all_records()
                 
        for i, record in enumerate(records):
            if record['username'] == username:
                # Check if deleted
                if record.get('deleted') == "TRUE":
                    # Reactivate Account
                    # Update password, name, email, deleted=FALSE, progress=0
                    # Row is i + 2 because headers are row 1 and enumerate is 0-indexed
                    row = i + 2
                    # Update cells: Pass(2), Name(3), Email(4), Progress(5), Deleted(6)
                    sheet.update_cell(row, 2, make_hashes(password))
                    sheet.update_cell(row, 3, name)
                    sheet.update_cell(row, 4, email)
                    sheet.update_cell(row, 5, 0)
                    sheet.update_cell(row, 6, "FALSE")
                    
                    # Send Welcome Email (Re-registration)
                    sent, msg = send_email(
                        email, 
                        "Welcome Back to Azundow Chatbot!", 
                        f"Hi {name},\n\nYour account '{username}' has been successfully reactivated!\n\nHappy Learning!"
                    )
                    return True, "Account reactivated successfully. Welcome back!"
                else:
                    return False, "Username already exists."
        
        # Append new user with progress = 0 and deleted = FALSE
        # Columns: username, password, name, email, progress, deleted
        sheet.append_row([username, make_hashes(password), name, email, 0, "FALSE"])
        
        # Send Welcome Email
        sent, msg = send_email(
            email, 
            "Welcome to Azundow Chatbot!", 
            f"Hi {name},\n\nWelcome to Azundow Intelligent Chatbot!\n\nYour username is: {username}\n\nHappy Learning!"
        )
        return True, msg
    except Exception as e:
        print(f"Register Error: {e}")
        return False, f"Error: {e}"

def login_user(username, password):
    """Logs in a user. Returns tuple (username, password, name, progress_index)."""
    sheet, error = get_db_connection()
    if not sheet:
        return None

    try:
        # Check actual headers first
        headers = sheet.row_values(1)
            
        records = sheet.get_all_records()

        hashed_pw = make_hashes(password)
        
        for i, record in enumerate(records):
            if record['username'] == username:
                pass
                
            if record['username'] == username and str(record['password']) == hashed_pw:
                # Check if deleted
                if record.get('deleted') == "TRUE":
                     return None
                     
                # Handle missing progress column gracefully
                progress = record.get('progress', 0)
                if progress == "" or progress is None:
                    progress = 0
                return [(record['username'], record['password'], record['name'], int(progress))]
        return None
    except Exception as e:
        print(f"Login Error: {e}")
        return None

def reset_password(username, email, new_password):
    """Resets password if username and email match."""
    sheet, error = get_db_connection()
    if not sheet:
        return False, "Database connection failed."

    try:
        records = sheet.get_all_records()
        cell = sheet.find(username)
        
        if cell:
            # Check if email matches (simulated verification)
            # Row index is cell.row, assuming email is in column 4 (D) based on init_db order?
            # Actually, init_db order is ["username", "password", "name", "email"]
            # So: Col 1=User, Col 2=Pass, Col 3=Name, Col 4=Email. 
            # Wait, `update_progress` assumed progress was column 4. Now Email is column 4?
            # Let's fix column assumption. We should find column index by header name to be safe, 
            # or stick to a convention.
            # Let's stick to appending email at the end: ["username", "password", "name", "progress", "email"]?
            # But the user might have existing data. Let's assume standard order:
            # User(1), Pass(2), Name(3), Email(4), Progress(5).
            
            # Let's check the record content first.
            row_data = sheet.row_values(cell.row)
            # We need to be careful about indices.
            # Let's use get_all_records to be safe about column names.
            # But we need row number to update.
            
            # Simplified approach: fetch row, check email at index 3 (4th col), update index 1 (2nd col)
            stored_email = sheet.cell(cell.row, 4).value
            if stored_email == email:
                # Generate Temporary Password
                chars = string.ascii_letters + string.digits
                temp_password = ''.join(random.choice(chars) for i in range(8))
                
                # Update DB
                sheet.update_cell(cell.row, 2, make_hashes(temp_password))
                
                # Send Email
                sent, msg = send_email(
                    email,
                    "Password Reset - Azundow Chatbot",
                    f"Hi,\n\nYour password has been reset.\n\nYour Temporary Password: {temp_password}\n\nPlease login and change it (change password feature coming soon) or just keep using this one."
                )
                if sent:
                    return True, msg
                else:
                    return False, msg
        return False, "User not found or email mismatch."
    except Exception as e:
        print(f"Reset PW Error: {e}")
        return False, f"Error: {e}"

def update_progress(username, new_index):
    """Updates the progress index for a user."""
    sheet, error = get_db_connection()
    if not sheet:
        return False
        
    try:
        cell = sheet.find(username)
        if cell:
            # Update 'progress' column. 
            # If headers are ["username", "password", "name", "email"], where is progress?
            # Usually gspread get_all_records handles extra columns fine.
            # But if we want to WRITE to it, we need a specific column.
            # Let's say Progress is Col 5.
            # If the sheet doesn't have a header for it, we might be writing to empty space.
            # Let's assume Col 5 for progress.
            sheet.update_cell(cell.row, 5, new_index)
            return True
        return False
    except Exception as e:
        print(f"Update Progress Error: {e}")
        return False

def delete_user(username):
    """Soft deletes a user by setting 'deleted' column to TRUE."""
    sheet, error = get_db_connection()
    if not sheet:
        return False, "Database connection failed."

    try:
        cell = sheet.find(username)
        if cell:
            # Update 'deleted' column. Assuming Col 6 based on init_db logic.
            sheet.update_cell(cell.row, 6, "TRUE")
            return True, "Account deleted successfully."
        return False, "User not found."
    except Exception as e:
        print(f"Delete User Error: {e}")
        return False, f"Error: {e}"
