# Import necessary libraries
import streamlit as st
import PyPDF2

# Function to extract text from PDF
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    content = ""
    for page_num in range(num_pages):
        content += pdf_reader.pages[page_num].extract_text()
    return content

# Streamlit app
def main():
    st.title("PDF Text Extractor")

    # File upload
    file = st.file_uploader("Upload a PDF file", type="pdf")

    if file is not None:
        # Read PDF and extract text
        content = read_pdf(file)

        # Display the content
        st.subheader("Extracted Text:")
        st.text(content)

if __name__ == "__main__":
    main()
