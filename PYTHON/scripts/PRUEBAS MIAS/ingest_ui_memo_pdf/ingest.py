
import util_funs.globalsettings as gs

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import DirectoryLoader


if __name__ ==  '__main__':

    loader = DirectoryLoader(gs.the_folders.DIR_PDF_FILES, glob='*.pdf')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(
        texts,
        embeddings,
        collection_name='pdf_files',
        persist_directory=gs.the_folders.DIR_PERSIST
        )

    # Save DB locally
    vector_store.persist()