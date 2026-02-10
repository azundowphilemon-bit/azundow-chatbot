import re

TUTORIAL_FILE = "documents/python_curriculum.md"

def get_topics():
    """Parses the tutorial file to return a list of topics (H1 headers)."""
    topics = []
    in_code_block = False
    try:
        with open(TUTORIAL_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        for line in lines:
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                continue
            
            # We treat H1 headers (# Header) as main topics
            # But ONLY if not inside a code block
            if not in_code_block and line.startswith("# ") and "Python Curriculum" not in line:
                topic = line.strip("# ").strip()
                if topic: # Ensure not empty
                    topics.append(topic)
                
        return topics
    except FileNotFoundError:
        return ["Introduction"] # Fallback

def get_topic_content(topic_name):
    """Returns the content for a specific topic."""
    content = ""
    is_capturing = False
    in_code_block = False
    
    try:
        with open(TUTORIAL_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        for line in lines:
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
            
            if not in_code_block and line.startswith("# "):
                current_topic = line.strip("# ").strip()
                if current_topic == topic_name:
                    is_capturing = True
                elif is_capturing:
                    # Stop capturing at the next H1
                    break
            
            if is_capturing:
                content += line
                
        return content
    except:
        return ""
