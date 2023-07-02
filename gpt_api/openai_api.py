# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_openai_api.ipynb.

# %% auto 0
__all__ = ['foo', 'load_api_key']

# %% ../nbs/00_openai_api.ipynb 3
def foo(): pass

# %% ../nbs/00_openai_api.ipynb 6
def load_api_key(path='../../.env'):
    dotenv_path = Path(path)
    load_dotenv(dotenv_path)
    API_KEY = os.getenv('API_KEY')  
    return API_KEY