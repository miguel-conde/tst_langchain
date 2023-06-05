import util_funs.globalsettings as gs

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import CSVLoader
from langchain.document_loaders import PyPDFLoader

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

    # make_vector_store(gs.the_folders.DIR_PDF_CSV_FILES, '*.pdf', 'pdf_files')
    # make_vector_store(gs.the_folders.DIR_PDF_CSV_FILES, '*.csv', 'csv_files')

    # loader_0 = CSVLoader(gs.the_files.CSV_FILES[0])
    # loader_1 = CSVLoader(gs.the_files.CSV_FILES[1])
    # index_creator = VectorstoreIndexCreator(vectorstore_kwargs={'persist_directory': gs.the_folders.DIR_PERSIST, 'collection_name': 'csv_files'})
    # docsearch = index_creator.from_loaders([loader_0, loader_1])
    # vectorstore=docsearch.vectorstore
    # vectorstore.persist()

    loader_CSV_0 = CSVLoader(gs.the_files.CSV_FILES[0])
    index_creator = VectorstoreIndexCreator(vectorstore_kwargs={'persist_directory': gs.the_folders.DIR_PERSIST, 'collection_name': 'csv_files_spain'})
    index_CSV = index_creator.from_loaders([loader_CSV_0])
    vectorstore_csv = index_CSV.vectorstore
    vectorstore_csv.persist()

    loader_CSV_1 = CSVLoader(gs.the_files.CSV_FILES[1])
    index_creator = VectorstoreIndexCreator(vectorstore_kwargs={'persist_directory': gs.the_folders.DIR_PERSIST, 'collection_name': 'csv_files_ue'})
    index_CSV = index_creator.from_loaders([loader_CSV_1])
    vectorstore_csv = index_CSV.vectorstore
    vectorstore_csv.persist()

    loader_PDF = PyPDFLoader(gs.the_files.PDF_FILES[0])
    index_creator = VectorstoreIndexCreator(vectorstore_kwargs={'persist_directory': gs.the_folders.DIR_PERSIST, 'collection_name': 'pdf_files'})
    index_PDF = index_creator.from_loaders([loader_PDF])
    vectorstore_pdf = index_PDF.vectorstore
    vectorstore_pdf.persist()
