"""Minimal example of exposing a skill over HTTP.

This is a reference implementation, not a production service - it has no
authentication, no rate limiting, and no request size limits. See SECURITY.md
before running it anywhere reachable outside your own machine.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from sdk.runner import run_skill
from sdk.providers import get_provider_from_env

app = FastAPI(title="Skills AI Webhook Example")


class SkillRequest(BaseModel):
    skill: str
    payload: dict


@app.post("/run-skill")
def run_skill_endpoint(req: SkillRequest):
    try:
        # Uses whichever PROVIDER is configured in the environment (see
        # .env.example) - mock by default, so nothing leaves the machine
        # unless you've explicitly set PROVIDER=anthropic or PROVIDER=openai.
        result = run_skill(req.skill, input_data=req.payload, provider=get_provider_from_env())
        return {"ok": True, "result": result}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/health")
def health():
    return {"status": "ok"}
