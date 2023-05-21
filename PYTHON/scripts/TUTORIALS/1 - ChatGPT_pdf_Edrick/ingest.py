# https://www.youtube.com/watch?v=FuqdVNB_8c0&list=PL9V0lbeJ69brU-ojMpU1Y7Ic58Tap0Cw6
# pip install PyPDF4

import os
from dotenv import load_dotenv

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from util_funs import parse_pdf
from util_funs import clean_text, merge_hyphenated_words
from util_funs import fix_newlines, remove_multiple_newlines, text_to_docs


if __name__ ==  '__main__':
    _ = load_dotenv() 


    # Step 1 - Parse PDF
    file_path = os.path.join(os.getcwd(), "data", "77009321.pdf")
    
    raw_pages, metadata = parse_pdf(file_path)

    # Step 2 - Create text chunks
    cleaning_functions = [
        merge_hyphenated_words,
        fix_newlines,
        remove_multiple_newlines
    ]

    cleaned_text_pdf = clean_text(raw_pages, cleaning_functions)
    document_chunks  = text_to_docs(cleaned_text_pdf, metadata)

    # Optional: reduce embedding cost by only using the first 23 pages
    document_chunks = document_chunks[:70]

    # Step 3 + 4: Generate embeddings and store them in DB
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(
        document_chunks,
        embeddings,
        collection_name="forecasting_ccb",
        persist_directory=os.path.join(os.getcwd(), "data", "chroma")
    )

    # Save DB locally
    vector_store.persist()