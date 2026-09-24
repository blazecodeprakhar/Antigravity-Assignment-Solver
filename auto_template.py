"""
Antigravity Intelligent Document Parser & Auto-Template Generator
Scans raw_file/*.docx, extracts questions, and generates solution starter code files in workspace/
"""

import os
import glob
import re
import docx

def parse_docx_questions(docx_path):
    doc = docx.Document(docx_path)
    questions = []
    
    pattern = re.compile(r'^\s*(\d+[\.\)]\s*.+|Problem\s*\d+.*|Query\s*\d+.*)', re.IGNORECASE)
    
    for p in doc.paragraphs:
        text = p.text.strip()
        if not text:
            continue
        if pattern.match(text) or ("Write" in text and len(text) > 15):
            questions.append(text)
            
    return questions

def generate_workspace_templates():
    workspace_root = os.path.dirname(os.path.abspath(__file__))
    raw_dir = os.path.join(workspace_root, "raw_file")
    workspace_dir = os.path.join(workspace_root, "workspace")
    
    os.makedirs(workspace_dir, exist_ok=True)
    
    raw_files = glob.glob(os.path.join(raw_dir, "*.docx"))
    if not raw_files:
        print("[!] No assignment docx found in raw_file/")
        return
        
    questions = parse_docx_questions(raw_files[0])
    print(f"[+] Found {len(questions)} problem questions in assignment document.")
    
    for idx, q in enumerate(questions, 1):
        py_filename = f"Problem{idx}.py"
        py_filepath = os.path.join(workspace_dir, py_filename)
        
        if os.path.exists(py_filepath):
            print(f"[=] {py_filename} already exists. Skipping template creation.")
            continue
            
        code_content = f"""def solution_problem_{idx}():
    print("Solution for Problem {idx}")

if __name__ == "__main__":
    solution_problem_{idx}()
"""
        with open(py_filepath, "w", encoding="utf-8") as f:
            f.write(code_content)
        print(f"[+] Created solution template: workspace/{py_filename}")

if __name__ == "__main__":
    generate_workspace_templates()
