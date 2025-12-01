from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
import read_csv_agent

# Create a logger instance to capture messages above DEBUG level in file in "gitignoreme/Logs/ folder under budget-variance-assistant folder  
log = Logfiles.get_logger(__name__)           
print(log.name)                                         
log.info(f"invoice_csv_agent is running")
# ' log.exception(\"This is exception logging")'


retry_config= types.HttpRetryOptions(
    attempts=2,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)

invoicefile = "TestFiles\Invoice_Oct2025.csv",
csv_tool  = AgentTool(read_csv_agent)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='invoice_csv_agent',
    description='A helpful assistant for user questions about invoice csv {invoicefile}.',
    instruction='Read the csv {invoicefile} and answer user questions such as get month of the invoices, amount by vendor, vendornames, etc. ',
    tools=[csv_tool]
)
