import util_funs.globalsettings as gs

from langchain.vectorstores.chroma import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.schema import HumanMessage, AIMessage


if __name__ ==  '__main__':
    
    model = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature="0",
        # verbose=True
    )
    embedding = OpenAIEmbeddings()

    vector_store = Chroma(
        collection_name='pdf_files',
        embedding_function=embedding,
        persist_directory=gs.the_folders.DIR_PERSIST
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        model,
        retriever=vector_store.as_retriever(),
        return_source_documents=True,
        # verbose=True,
        )
    
    chat_history = []

    while True:
        print()
        question = input("Question: ")

        # Generate answer
        response = qa_chain({"question": question, "chat_history": chat_history})

        # Retrieve answer
        answer = response["answer"]
        source = response["source_documents"]
        chat_history.append(HumanMessage(content=question))
        chat_history.append(AIMessage(content=answer))

        # Display answer
        print("\n\nSources:\n")
        for document in source:
            # print(f"Page: {document.metadata['page_number']}")
            # print(f"Text chunk: {document.page_content[:160]}...\n")
            print(f"\nDocument: {document.page_content}\n")
            print(f"\Source: {document.metadata['source']}\n")
        print(f"\n\nAnswer\n: {answer}")