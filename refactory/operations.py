# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_operations.ipynb.

# %% auto 0
__all__ = ['optimization', 'clean_code', 'big_o', 'runtime', 'bugs']

# %% ../nbs/01_operations.ipynb 4
import openai
from .openai_api import *

# %% ../nbs/01_operations.ipynb 6
openai.api_key = load_api_key()

# %% ../nbs/01_operations.ipynb 7
def optimization(raw_file:str, metric:str) -> str:
    chat_response = openai_chat(f'Optimize this code with regard to the following metric: {metric}. Only include code in your response', raw_file)
    optimized_code = chat_response.choices[0].message.content
    return optimized_code

# %% ../nbs/01_operations.ipynb 8
# Readability & maintainability
def clean_code(python_file:str) -> str:
    return optimization(python_file, metric='clean code')

# %% ../nbs/01_operations.ipynb 10
def big_o(python_file:str):
    return optimization(python_file, metric='big O space and time complexity')

# %% ../nbs/01_operations.ipynb 11
def runtime(python_file:str):
    return optimization(python_file, metric='runtime')

# %% ../nbs/01_operations.ipynb 12
def bugs(python_file:str):
    return optimization(python_file, metric='bugs') 
