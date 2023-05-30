# https://dev.to/ngonidzashe/chat-with-your-csv-visualize-your-data-with-langchain-and-streamlit-ej7

import streamlit as st
import pandas as pd
import json

from util_funs.agent_csv import query_agent, create_agent, API_KEY
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI


def decode_response(response: str) -> dict:
    """This function converts the string response from the model to a dictionary object.

    Args:
        response (str): response from the model

    Returns:
        dict: dictionary with response data
    """
    return json.loads(response)

def write_response(response_dict: dict):
    """
    Write a response from an agent to a Streamlit app.

    Args:
        response_dict: The response from the agent.

    Returns:
        None.
    """

    # Check if the response is an answer.
    if "answer" in response_dict:
        st.write(response_dict["answer"])

    # Check if the response is a bar chart.
    if "bar" in response_dict:
        data = response_dict["bar"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.bar_chart(df)

    # Check if the response is a line chart.
    if "line" in response_dict:
        data = response_dict["line"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.line_chart(df)

    # Check if the response is a table.
    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)


st.title("👨‍💻 Chat with your CSV")

st.write("Please upload your CSV file below.")

data = st.file_uploader("Upload a CSV")

query = st.text_area("Insert your query")

if st.button("Submit Query", type="primary"):
    # # Create an agent from the CSV file.
    # agent = create_agent(data)

    # # Query the agent.
    # response = query_agent(agent=agent, query=query)
    # print(response)

    # # Decode the response.
    # decoded_response = decode_response(response)

    # # Write the response to the Streamlit app.
    # write_response(decoded_response)

    agent = create_csv_agent(OpenAI(temperature=0), data, verbose=True)

    response = agent.run(query)

    st.write(response)

# streamlit run ui_csv.py