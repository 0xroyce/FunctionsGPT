import os
from dotenv import load_dotenv
load_dotenv()
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=Singleton):

    def __init__(self):
        # API configurations
        self.smart_llm_model = self._get_env("SMART_LLM_MODEL")
        self.fast_llm_model = self._get_env("FAST_LLM_MODEL")
        self.openai_api_key = self._get_env("OPENAI_API_KEY")

    def _get_env(self, key: str) -> str:
        """Retrieve environment variable and throw error if not found."""
        value = os.getenv(key)
        if not value:
            raise EnvironmentError(f"{key} not found in environment variables.")
        return value

    def update_config(self, **kwargs):
        """Update configurations using keyword arguments."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)