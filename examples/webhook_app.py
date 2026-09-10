import json
import tempfile
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from skills_ai.runner import run_skill
from skills_ai.providers import MockProvider

app = FastAPI(title="Skills AI Webhook Example")


class SkillRequest(BaseModel):
    skill: str
    payload: dict


@app.post("/run-skill")
def run_skill_endpoint(req: SkillRequest):
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as tmp:
            json.dump(req.payload, tmp)
            temp_path = tmp.name

        result = run_skill(req.skill, input_path=temp_path, provider=MockProvider())

        Path(temp_path).unlink(missing_ok=True)
        return {"ok": True, "result": result}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/health")
def health():
    return {"status": "ok"}
