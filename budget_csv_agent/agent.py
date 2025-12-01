from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from readcsv_agent.agent import read_csv_agent

budgetfile = "TestFiles\Invoice_Oct2025.csv",

root_agent = Agent(
    model='gemini-2.5-flash',
    name='budget_csv_agent',
    description='A helpful assistant for user questions about invoice csv {budgetfile}.',
    instruction='Read the csv {budgetfile} and answer user questions such as - ' \
    'total budget amount for the month, ' \
    'budget amount by vendor, ' \
    'get vendornames, ' \
    'get budget amount by vendor and month, etc. ',
    tools=[AgentTool(read_csv_agent)]
)
