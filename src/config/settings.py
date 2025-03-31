import os
from dotenv import load_dotenv

# === 🔧 Environment Variables & Configuration ===

# Load environment variables from the secret config file
load_dotenv("Config/.env.secret")

# === 🔧 LLM Configuration Check ===
def has_gpt_4o_config() -> bool:
    """
    Check if the GPT-4o configuration is complete.
    """
    return all([
        os.getenv("AZURE_OPENAI_API_KEY"),
        os.getenv("AZURE_OPENAI_ENDPOINT"),
        os.getenv("AZURE_GPT4O_DEPLOYMENT"),
        os.getenv("AZURE_GPT4O_API_VERSION"),
    ])

def has_gpt_4o_mini_config() -> bool:
    """
    Check if the GPT-4o-Mini configuration is complete.
    """
    return all([
        os.getenv("AZURE_OPENAI_API_KEY"),
        os.getenv("AZURE_OPENAI_ENDPOINT"),
        os.getenv("AZURE_GPT4OMINI_DEPLOYMENT"),
        os.getenv("AZURE_GPT4OMINI_API_VERSION"),
    ])

def has_mistral_large_config() -> bool:
    """
    Check if the Mistral-Large configuration is complete.
    """
    return all([
        os.getenv("MISTRAL_LARGE_API_KEY"),
        os.getenv("MISTRAL_LARGE_ENDPOINT"),
        os.getenv("MISTRAL_LARGE_DEPLOYMENT"),
    ])

def has_mistral_config() -> bool:
    """
    Check if the Mistral-Nemo configuration is complete.
    """
    return all([
        os.getenv("MISTRAL_API_KEY"),
        os.getenv("MISTRAL_ENDPOINT"),
    ])

def has_llama3_config() -> bool:
    """
    Check if the Llama3 configuration is complete.
    """
    return all([
        os.getenv("LLAMA3_API_KEY"),
        os.getenv("LLAMA3_ENDPOINT"),
    ])

# === 🌍 API Keys & Endpoints ===
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

AZURE_GPT4O_DEPLOYMENT = os.getenv("AZURE_GPT4O_DEPLOYMENT")
AZURE_GPT4O_API_VERSION = os.getenv("AZURE_GPT4O_API_VERSION")

AZURE_GPT4OMINI_DEPLOYMENT = os.getenv("AZURE_GPT4OMINI_DEPLOYMENT")
AZURE_GPT4OMINI_API_VERSION = os.getenv("AZURE_GPT4OMINI_API_VERSION")

MISTRAL_LARGE_API_KEY = os.getenv("MISTRAL_LARGE_API_KEY")
MISTRAL_LARGE_ENDPOINT = os.getenv("MISTRAL_LARGE_ENDPOINT")
MISTRAL_LARGE_DEPLOYMENT = os.getenv("MISTRAL_LARGE_DEPLOYMENT")

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_ENDPOINT = os.getenv("MISTRAL_ENDPOINT")

LLAMA3_API_KEY = os.getenv("LLAMA3_API_KEY")
LLAMA3_ENDPOINT = os.getenv("LLAMA3_ENDPOINT")