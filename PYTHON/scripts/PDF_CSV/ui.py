import util_funs.globalsettings as gs
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

from langchain.vectorstores.chroma import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import HumanMessage, AIMessage

from langchain.agents import AgentType, initialize_agent

from langchain import LLMMathChain, SerpAPIWrapper
from langchain.tools import BaseTool, StructuredTool, Tool, tool

from langchain.memory import ConversationBufferMemory

## 

model = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature="0",
        # verbose=True
    )

embedding = OpenAIEmbeddings()

vector_store = Chroma(
    collection_name='pdf_csv_files',
    embedding_function=embedding,
    persist_directory=gs.the_folders.DIR_PERSIST
    )

qa_chain = ConversationalRetrievalChain.from_llm(
# qa_chain = load_qa_chain(
    model,
    retriever=vector_store.as_retriever(),
    return_source_documents=False,
    memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    # verbose=True,
    )

##
# Load the tool configs that are needed.
tools = [
    Tool.from_function(
        func=qa_chain.run,
        name = "Q&A",
        description="useful for when you need to answer questions",
        # coroutine= ... <- you can specify an async method if desired as well
    ),
]

chat_history = []

## Creamos el agente CSV
agent = create_csv_agent(model, gs.the_files.CSV_FILES[0], verbose=True, tools = tools)
agent2 = initialize_agent(tools, model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION , verbose=True)

# agent.run("how many rows are there?")
# agent.run("show 4 first rows")
# agent.run("tell me columns in CSVs'")
# agent2.run("tell me columns in CSVs'")

# agent.run("Que consecuencias ha tenido la guerra de Ucrania?'")
agent2.run("Que consecuencias ha tenido la guerra de Ucrania?'")