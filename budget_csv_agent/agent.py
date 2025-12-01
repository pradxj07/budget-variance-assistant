from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool
from pydantic import BaseModel
import Logfiles
from google.genai import types
import read_csv_agent

# Create a logger instance to capture messages above DEBUG level in file in "gitignoreme/Logs/ folder under budget-variance-assistant folder  
log = Logfiles.get_logger(__name__)           
print(log.name)                                         
log.info(f"budget_csv_agent is running")


retry_config= types.HttpRetryOptions(
    attempts=2,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)

budgetfile = "TestFiles\testbudget-oct-dec2025.csv"
# csv_tool  = AgentTool(read_csv_agent)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='budget_csv_agent',
    description='A helpful assistant for user questions about invoice csv {budgetfile}.',
    instruction='Read the csv {budgetfile} and answer user questions such as - ' \
    'total budget amount for the month, ' \
    'budget amount by vendor, ' \
    'get vendornames, ' \
    'get budget amount by vendor and month, etc. ',
    tools=[read_csv_agent]
)
