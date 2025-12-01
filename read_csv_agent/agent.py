from google.adk.agents.llm_agent import Agent
import Logfiles
from google.genai import types
from google.adk.models.google_llm import Gemini

## Wrapper agent to read invoices 

# function to read invoice data from CSV
def get_invoice_data(inpcsvfile):
    # Function to read and return data from the CSV file
    import pandas as pd

    df = pd.read_csv(inpcsvfile)
    print(df.to_string())     
    return df

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

inpcsvfile = "TestFiles/Invoice_Oct2025.csv",

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    name='read_csv_agent',
    description='A helpful assistant to read data from csv and for user questions regarding {inpcsvfile}.',
    instruction='Answer user questions to the best of your knowledge about dataframe created from csv such as amounts aand months and amounts by vendors.',
    tools=[get_invoice_data]
)
