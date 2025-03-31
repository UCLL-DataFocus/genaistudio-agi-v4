# llama3.py
from dataclasses import dataclass
from typing import Optional, cast

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, ChatCompletions
from azure.core.credentials import AzureKeyCredential

@dataclass
class LLMResult:
    """
    A simple wrapper for the model's response,
    providing a `.content` attribute for easy access.
    """
    content: str


class Llama3LLM:
    """
    A self-contained class to query a Llama3 model hosted on Azure Inference.
    Assumes exactly one Llama3 model is deployed on your endpoint (no deployment_name).
    """

    def __init__(
        self,
        api_key: str,
        endpoint: str,
        max_tokens: int = 2048,
        temperature: float = 0.8,
        top_p: float = 0.1,
        presence_penalty: float = 0.0,
        frequency_penalty: float = 0.0,
        system_prompt: str = "You are a helpful assistant."
    ) -> None:
        """
        Args:
            api_key (str): Azure Inference access key.
            endpoint (str): The HTTPS endpoint for your Azure Inference resource.
            max_tokens (int): Max tokens for the response (default 2048).
            temperature (float): Sampling temperature (default 0.8).
            top_p (float): Nucleus sampling probability (default 0.1).
            presence_penalty (float): Presence penalty (default 0.0).
            frequency_penalty (float): Frequency penalty (default 0.0).
            system_prompt (str): A default system message for the model context.
        """
        self.api_key = api_key
        self.endpoint = endpoint
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.presence_penalty = presence_penalty
        self.frequency_penalty = frequency_penalty
        self.system_prompt = system_prompt

        self.client = ChatCompletionsClient(
            endpoint=self.endpoint,
            credential=AzureKeyCredential(self.api_key),
        )

    def invoke(self, user_prompt: str) -> LLMResult:
        """
        Sends a single turn to the Llama3 model and returns a result object.

        Args:
            user_prompt (str): The user's message.

        Returns:
            LLMResult: An object with `.content` holding the model's text response.
        """
        messages = [
            SystemMessage(content=self.system_prompt),
            UserMessage(content=user_prompt),
        ]

        try:
            response = self.client.complete(
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                top_p=self.top_p,
                presence_penalty=self.presence_penalty,
                frequency_penalty=self.frequency_penalty,
            )
            completions = cast(ChatCompletions, response)
            answer = completions.choices[0].message.content
            return LLMResult(content=answer)
        except Exception as e:
            return LLMResult(content=f"Error during Llama3 invoke: {str(e)}")
