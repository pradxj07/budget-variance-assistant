from google.adk.agents.llm_agent import Agent
from google.adk.agents import ParallelAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.google_llm import Gemini
from budget_csv_agent import budget_csv_agent
from invoice_csv_agent import invoice_csv_agent
import Logfiles
from google.genai import types

# Create a logger instance to capture messages above DEBUG level in file in "gitignoreme/Logs/ folder under budget-variance-assistant folder  
log = Logfiles.get_logger(__name__)           
print(log.name)                                         
log.info(f"parallel_csv_agent is running")
# ' log.exception(\"This is exception logging")'

retry_config=types.HttpRetryOptions(
    attempts=2,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)
root_agent = ParallelAgent(
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    name='parallel_csv_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge about budget and invoice csv files.',
    tools=[AgentTool(budget_csv_agent),AgentTool(invoice_csv_agent)]

)
