from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from readcsv_agent.agent import read_csv_agent

invoicefile = "TestFiles\Invoice_Oct2025.csv",

root_agent = Agent(
    model='gemini-2.5-flash',
    name='invoice_csv_agent',
    description='A helpful assistant for user questions about invoice csv {invoicefile}.',
    instruction='Read the csv {invoicefile} and answer user questions such as get month of the invoices, amount by vendor, vendornames, etc. ',
    tools=[AgentTool(read_csv_agent)]
)
