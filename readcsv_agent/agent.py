from google.adk.agents.llm_agent import Agent
# import logging
import Logfiles
from google.genai import types
from google.adk.models.google_llm import Gemini

## Wrapper agent to read invoices 

# function to read invoice data from CSV
def get_invoice_data(invoicefile):
    # Function to read and return invoice data from the CSV file
    import pandas as pd

    df = pd.read_csv(invoicefile)

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

invoicefile = "TestFiles\Invoice_Oct2025.csv",

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    name='readcsv_agent',
    description='A helpful assistant for user questions regarding {invoicefile}.',
    instruction='Answer user questions to the best of your knowledge about dataframe created from csv',
    tools=[get_invoice_data({invoicefile})]
)




