from google.adk.agents.llm_agent import Agent
import parallel_csv_agent
import Logfiles
from google.genai import types

# Create a logger instance to capture messages above DEBUG level in file in "gitignoreme/Logs/ folder under budget-variance-assistant folder  
log = Logfiles.get_logger(__name__)           
print(log.name)                                         
log.info(f"this is info logging")
# ' log.exception(\"This is exception logging")'

retry_config= types.HttpRetryOptions(
    attempts=2,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504], # Retry on these HTTP errors
)


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant that runs csv agenets in parallel to get budget variance information.',
    instruction="Take input from user about which month's budget variance is required and run the casv agents  the same",
    tools=[parallel_csv_agent]
)
