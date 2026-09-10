import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()


class Provider:
    """Abstract provider interface."""

    def generate(self, prompt: str) -> Any:
        raise NotImplementedError()


class MockProvider(Provider):
    """Simple mock provider that returns a deterministic response for testing."""

    def generate(self, prompt: str) -> dict:
        # Return a simple structured response that skills can parse in tests
        return {
            "raw": prompt,
            "assessment": {
                "risk_score": 7,
                "top_drivers": ["usage_decline", "exec_change"],
                "recommended_actions": ["exec_review", "resolve_issue"]
            }
        }


class OpenAIProvider(Provider):
    """Provider that calls OpenAI's ChatCompletion API.

    Requires environment variables:
    - OPENAI_API_KEY
    - OPENAI_MODEL (optional, defaults to gpt-3.5-turbo)
    """

    def __init__(self):
        try:
            import openai
        except Exception as e:
            raise RuntimeError("openai package is not installed. Install requirements.txt") from e

        self._openai = openai
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set in environment")
        self._openai.api_key = api_key
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

    def generate(self, prompt: str) -> Any:
        # Use chat completion with a single user message
        resp = self._openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800,
        )
        # Return assistant content
        choices = resp.get("choices")
        if choices and len(choices) > 0:
            return choices[0].get("message", {}).get("content")
        return resp


def get_provider_from_env() -> Provider:
    prov = os.getenv("PROVIDER", "mock").lower()
    if prov == "openai":
        return OpenAIProvider()
    # default to mock
    return MockProvider()
