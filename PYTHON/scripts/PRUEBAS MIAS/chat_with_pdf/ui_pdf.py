import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
# from langchain.vectorstores import FAISS
from langchain.vectorstores import Chroma
import os

import util_funs.globalsettings as gs

st.title("👨‍💻 Chat with your PDF")

st.write("Please upload your PDF file below.")

uploaded_file = st.file_uploader("Upload a PDF", type = "pdf")

query = st.text_area("Insert your query")

if uploaded_file is not None:
    save_folder = gs.the_folders.DIR_DATA
    save_path = os.path.join(save_folder, "tmp_file.pdf")
    with open(save_path, mode='wb') as w:
        w.write(uploaded_file.getvalue())
        w.close()

    st.write("Reading " + uploaded_file.name + "...")

    # Document Loader
    loader = PyPDFLoader(save_path)
    documents = loader.load()

    # Text Splitter
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Embeddings
    # embeddings = HuggingFaceEmbeddings()
    embeddings = OpenAIEmbeddings()
    # db = FAISS.from_documents(docs, embeddings)
    db = Chroma.from_documents(docs, embeddings)

    # Q&A chain
    retriever = db.as_retriever()

if st.button("Submit Query", type="primary"):

    qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)

    response = qa_chain.run(query)

    st.write(response)

# streamlit run ui_pdf.py