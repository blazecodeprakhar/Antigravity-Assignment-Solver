"""
Antigravity PDF Export Helper Module
Converts finalized .docx assignments in final_output/ into PDF format (.pdf) using Word COM / docx2pdf
"""

import os
import glob
import sys

def convert_docx_to_pdf():
    workspace_root = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(workspace_root, "final_output")
    
    docx_files = glob.glob(os.path.join(output_dir, "*.docx"))
    docx_files = [f for f in docx_files if not os.path.basename(f).startswith("~$")]
    
    if not docx_files:
        print("[!] No completed docx file found in final_output/")
        return
        
    target_docx = docx_files[0]
    target_pdf = os.path.splitext(target_docx)[0] + ".pdf"
    
    print(f"[+] Exporting PDF for: {os.path.basename(target_docx)}")
    
    try:
        import win32com.client
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(os.path.abspath(target_docx))
        doc.SaveAs(os.path.abspath(target_pdf), FileFormat=17) # 17 = wdFormatPDF
        doc.Close()
        word.Quit()
        print(f"[SUCCESS] PDF successfully generated at: {target_pdf}")
    except Exception as e:
        print(f"[!] PDF export via Word COM skipped/not available: {e}")

if __name__ == "__main__":
    convert_docx_to_pdf()
