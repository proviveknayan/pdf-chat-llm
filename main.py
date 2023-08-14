import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter ## to split the text into smaller chunks

## get the list of PDF(s) in the root directory
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]

## function to get the text from the PDF(s)
def get_pdf_text(pdf_files):
    text = ""
    for pdf in pdf_files:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

## function to split the text into smaller chunks
def get_text_chunks(pdf_text):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    text_chunks = text_splitter.split_text(pdf_text)
    return text_chunks

def main():
    st.set_page_config(page_title="Chat With Your PDF(s)", page_icon=":sunglasses:")

    st.header("Chat With Your PDF(s) :sunglasses:")
    st.text_input("Ask a question to your document(s):")
    
    with st.sidebar:
        st.subheader("Your Documents")
        st.write(f'Found {len(pdf_files)} PDF file(s).')
        st.write('- ' + '\n- '.join(pdf_files))
        with st.spinner("Processing the PDFs"):

            ## get the text from PDF(s)
            pdf_text = get_pdf_text(pdf_files)
            #st.write(pdf_text)

            ## split the text into smaller chunks
            text_chunks = get_text_chunks(pdf_text)
            #st.write(text_chunks)

            ## create vector store for the chunks

if __name__ == '__main__':
    main()