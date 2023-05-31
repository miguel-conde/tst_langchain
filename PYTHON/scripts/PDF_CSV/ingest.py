import util_funs.globalsettings as gs

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader

def make_vector_store(folder, patttern, collection_name):
    
    loader = DirectoryLoader(folder, glob=patttern)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(
        texts,
        embeddings,
        collection_name=collection_name,
        persist_directory=gs.the_folders.DIR_PERSIST
        )

    # Save DB locally
    vector_store.persist()


if __name__ ==  '__main__':

    # loader = DirectoryLoader(gs.the_folders.DIR_PDF_CSV_FILES, glob='*.pdf')
    # documents = loader.load()
    # text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=0)
    # texts = text_splitter.split_documents(documents)
    
    # embeddings = OpenAIEmbeddings()
    # vector_store = Chroma.from_documents(
    #     texts,
    #     embeddings,
    #     collection_name='pdf_csv_files',
    #     persist_directory=gs.the_folders.DIR_PERSIST
    #     )

    # # Save DB locally
    # vector_store.persist()

    make_vector_store(gs.the_folders.DIR_PDF_CSV_FILES, '*.pdf', 'pdf_files')
    make_vector_store(gs.the_folders.DIR_PDF_CSV_FILES, '*.csv', 'csv_files')