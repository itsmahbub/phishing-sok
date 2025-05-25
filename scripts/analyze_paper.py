import os
import pathlib
import tempfile
from typing import List

import google.generativeai as genai
from PyPDF2 import PdfReader

# Possible questions
# 1. Realistic environments?
# 2. New phishing detection?
# 3. cross-dataset evaluation
# 4. temporal split
# 5. client-side/lightweight

# Optional: Configure API key through environment variable
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("Warning: Google API key not found in environment variables. "
          "Please set the GOOGLE_API_KEY environment variable.")
    # You can also directly assign your API key here, but it's less secure:
    # GOOGLE_API_KEY = "YOUR_API_KEY"
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini Pro model
model = genai.GenerativeModel('gemini-pro')

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts text content from a PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except FileNotFoundError:
        print(f"Error: PDF file not found at {pdf_path}")
        return ""
    return text

def ask_question(document_content: str, question: str) -> str:
    """Sends a question about the document content to the Gemini model."""
    prompt = f"Based on the following document:\n\n{document_content}\n\nAnswer the question: {question}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during Gemini API call: {e}"

def main():
    pdf_path = input("Enter the path to the PDF document: ")
    document_content = extract_text_from_pdf(pdf_path)

    if not document_content:
        return

    print("\nDocument loaded. Let's start asking questions.\n")

    questions = [
        "What is the main topic of this paper?",
        "What are the key findings or contributions?",
    ]

    for i, question in enumerate(questions):
        answer = ask_question(document_content, question)
        print(f"Question {i+1}: {question}")
        print(f"Answer: {answer}\n")

        # Example of adaptive questioning based on the previous answer
        if i == 0:
            follow_up_question = f"Based on the main topic '{answer.strip()}', what specific methods or approaches were used?"
            follow_up_answer = ask_question(document_content, follow_up_question)
            print(f"Follow-up Question: {follow_up_question}")
            print(f"Answer: {follow_up_answer}\n")

if __name__ == "__main__":
    main()