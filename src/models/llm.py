from typing import Any, Dict, List

from langchain_openai import AzureChatOpenAI 
from src.models.custom.llama3 import Llama3LLM 
from src.models.custom.mistral_large import MistralLargeLLM 
from langchain_mistralai.chat_models import ChatMistralAI 
from src.config.settings import (
    AZURE_GPT4O_DEPLOYMENT,
    AZURE_GPT4O_API_VERSION,
    has_gpt_4o_config,
    AZURE_GPT4OMINI_DEPLOYMENT,
    AZURE_GPT4OMINI_API_VERSION,
    has_gpt_4o_mini_config,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    MISTRAL_LARGE_API_KEY,
    MISTRAL_LARGE_ENDPOINT,
    MISTRAL_LARGE_DEPLOYMENT,
    has_mistral_large_config,
    MISTRAL_API_KEY,
    MISTRAL_ENDPOINT,
    has_mistral_config,
    LLAMA3_API_KEY,
    LLAMA3_ENDPOINT,
    has_llama3_config,
)

# === 🤖 LLM Model Manager ===
# This module manages and caches instances of different LLMs for efficient reuse.
_AVAILABLE_MODELS = []

if has_gpt_4o_config():
    _AVAILABLE_MODELS.append("gpt-4o")

if has_gpt_4o_mini_config():
    _AVAILABLE_MODELS.append("gpt-4o-mini")

if has_mistral_large_config():
    _AVAILABLE_MODELS.append("mistral-large")

if has_mistral_config():
    _AVAILABLE_MODELS.append("mistral-nemo")

if has_llama3_config():
    _AVAILABLE_MODELS.append("llama3")

# Cache to store LLM instances and avoid redundant instantiations
_llm_cache: Dict[str, Any] = {}

def get_llm(model_name: str) -> Any:
    """
    Retrieves an LLM instance from the cache if available;
    otherwise, creates one and stores it for future reuse.

    Supported models:
    - "gpt-4o-mini": Azure OpenAI GPT-4o-mini model

    Args:
        model_name (str): The name of the model to retrieve.

    Returns:
        Any: The initialized LLM instance.
    """
    if model_name in _llm_cache:
        return _llm_cache[model_name]

    if model_name == "gpt-4o":
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,   # type: ignore
            azure_deployment=AZURE_GPT4O_DEPLOYMENT,
            api_version=AZURE_GPT4O_API_VERSION,
        )
    
    if model_name == "gpt-4o-mini":
        llm = AzureChatOpenAI(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,   # type: ignore
            azure_deployment=AZURE_GPT4OMINI_DEPLOYMENT,
            api_version=AZURE_GPT4OMINI_API_VERSION,
        )
    
    if model_name == "mistral-large":
        llm = MistralLargeLLM(
            api_key=MISTRAL_LARGE_API_KEY,
            endpoint=MISTRAL_LARGE_ENDPOINT,
            deployment_name=MISTRAL_LARGE_DEPLOYMENT,
        )
    
    if model_name == "mistral-nemo":
        llm = ChatMistralAI(
            api_key=MISTRAL_API_KEY,
            base_url=MISTRAL_ENDPOINT,
        )
    
    if model_name == "llama3":
        llm = Llama3LLM(
            api_key=LLAMA3_API_KEY,
            endpoint=LLAMA3_ENDPOINT,
        )

    # Store the LLM instance in cache
    _llm_cache[model_name] = llm
    return llm

def list_supported_models() -> List[str]:
    return _AVAILABLE_MODELS
