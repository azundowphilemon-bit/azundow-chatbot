import auth
import os

# Use a test database
auth.DB_NAME = "test_users.db"

# Clean up previous test db if exists
if os.path.exists(auth.DB_NAME):
    try:
        os.remove(auth.DB_NAME)
    except PermissionError:
        print(f"Warning: Could not remove {auth.DB_NAME}, it might be in use.")

print("Initializing DB...")
auth.init_db()

print("Testing Registration...")
# Register a new user
success = auth.register_user("testuser", "password123", "Test User")
if success:
    print("Registration Successful: PASS")
else:
    print("Registration Failed: FAIL")

# Try registering duplicate
success_dup = auth.register_user("testuser", "password123", "Test User 2")
if not success_dup:
    print("Duplicate Registration Prevention: PASS")
else:
    print("Duplicate Registration Prevention: FAIL")

print("Testing Login...")
# Login with correct credentials
user = auth.login_user("testuser", "password123")
if user and user[0][0] == "testuser":
    print("Login Correct: PASS")
else:
    print("Login Correct: FAIL")

# Login with wrong password
user_wrong = auth.login_user("testuser", "wrongpass")
if not user_wrong:
    print("Login Wrong Password: PASS")
else:
    print("Login Wrong Password: FAIL")

# Login with non-existent user
user_none = auth.login_user("nonexistent", "password123")
if not user_none:
    print("Login Non-existent: PASS")
else:
    print("Login Non-existent: FAIL")

# Cleanup
if os.path.exists(auth.DB_NAME):
    try:
        os.remove(auth.DB_NAME)
    except PermissionError:
        print(f"Warning: Could not remove {auth.DB_NAME} after tests.")
