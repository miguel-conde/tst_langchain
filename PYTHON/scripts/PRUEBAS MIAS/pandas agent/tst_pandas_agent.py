import util_funs.globalsettings as gs

from langchain.agents import create_pandas_dataframe_agent

from langchain.llms import OpenAI
import pandas as pd

df = pd.read_csv(gs.the_files.PROBE_CSV)

agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)

# agent.run("how many rows are there?")
# agent.run("show 4 first rows")
agent.run("plot a barchart for 'Sex'")