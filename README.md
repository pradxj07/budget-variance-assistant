# prad-google-ai-agent-learning

The aim of this repository is to hold the capstone project and other artefacts created during practice of agent creation from google ai agent course

The project was created using Windows 10 machine via Ubuntu WSL using VSCode with following specifications -
Version: 1.105.1 (system setup)
Commit: 7d842fb85a0275a4a8e4d7e040d2625abbf7f084
Date: 2025-10-14T22:33:36.618Z
Electron: 37.6.0
ElectronBuildId: 12502201
Chromium: 138.0.7204.251
Node.js: 22.19.0
V8: 13.8.258.32-electron.0
OS: Windows_NT x64 10.0.19045

Steps - 
Create github project
Clone to local folder  
Create virtual environment  (https://docs.python.org/3/library/venv.html)
Pip Install from requirements.txt
In order to use kaggle api in your local machine, please follow the instructions given in https://www.kaggle.com/discussions/questions-and-answers/357399 to import kaggle_secrets
i.e. 
    - Download the kaggle.json token from Settings -> Create New Token.
    - Place the kaggle.json file in the current directory.
    - Run the following code to set up the token:
        !mkdir -p ~/.kaggle/ && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json


# Creating agents 
To create an agent, Follow instructions given in https://google.github.io/adk-docs/get-started/python/#run-your-agent to create a basic agent. For example, - 
adk create my-simple-agent
Enter Model 1 , 11
For Google gemini, enter the api key created in AI studio. 
Ensure you add .env file of the agent folder to the .gitignore file

Owner agent - budget_variance



## readcsv_agent #
Tool to read a csv and asnwer questions about them 
https://docs.langchain.com/oss/python/integrations/tools/pandas
https://github.com/google/adk-python/issues/


invoice_csv_agent - 
Wrapper/ Parent agent that calls read_csv agent to read invoices data

budget_csv_agent - 
Wrapper/Parent agent that calls read_csv agent to read budget data

