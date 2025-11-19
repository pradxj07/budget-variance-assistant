from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant to find budget variance ',
    instruction='Take input from user about which month's budget variance is required and print the same',',
)
