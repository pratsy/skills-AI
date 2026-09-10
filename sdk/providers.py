import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()


class Provider:
    """Abstract provider interface."""

    def generate(self, prompt: str) -> Any:
        raise NotImplementedError()


class MockProvider(Provider):
    """Deterministic provider for tests and local development - no API key required."""

    def generate(self, prompt: str) -> dict:
        return {
            "raw": prompt,
            "assessment": {
                "risk_score": 7,
                "top_drivers": ["usage_decline", "exec_change"],
                "recommended_actions": ["exec_review", "resolve_issue"],
            },
        }


class AnthropicProvider(Provider):
    """Provider that calls the Claude API.

    Requires:
    - ANTHROPIC_API_KEY
    - ANTHROPIC_MODEL (optional, defaults to claude-sonnet-5)
    """

    def __init__(self):
        try:
            from anthropic import Anthropic
        except ImportError as e:
            raise RuntimeError(
                "anthropic package is not installed. Install requirements.txt"
            ) from e

        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set in environment")
        self._client = Anthropic(api_key=api_key)
        self.model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5")

    def generate(self, prompt: str) -> Any:
        resp = self._client.messages.create(
            model=self.model,
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}],
        )
        if resp.content and len(resp.content) > 0:
            return resp.content[0].text
        return resp


class OpenAIProvider(Provider):
    """Provider that calls the OpenAI chat completions API.

    Requires:
    - OPENAI_API_KEY
    - OPENAI_MODEL (optional, defaults to gpt-4o-mini)
    """

    def __init__(self):
        try:
            from openai import OpenAI
        except ImportError as e:
            raise RuntimeError(
                "openai package is not installed. Install requirements.txt"
            ) from e

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set in environment")
        self._client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def generate(self, prompt: str) -> Any:
        resp = self._client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
        )
        if resp.choices and len(resp.choices) > 0:
            return resp.choices[0].message.content
        return resp


PROVIDERS = {
    "mock": MockProvider,
    "anthropic": AnthropicProvider,
    "openai": OpenAIProvider,
}


def get_provider_from_env() -> Provider:
    name = os.getenv("PROVIDER", "mock").lower()
    provider_cls = PROVIDERS.get(name)
    if provider_cls is None:
        raise ValueError(
            f"Unknown PROVIDER '{name}'. Supported: {', '.join(PROVIDERS)}"
        )
    return provider_cls()
