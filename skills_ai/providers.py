from typing import Any


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
