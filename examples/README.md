# Examples

## Local CLI usage

```bash
PYTHONPATH=. python -m skills_ai.runner renewal_risk_scorer --input examples/fixtures/renewal_input.json
```

## Webhook example

```bash
pip install fastapi uvicorn
uvicorn examples.webhook_app:app --reload
```

Then call:

```bash
curl -X POST http://127.0.0.1:8000/run-skill \
  -H 'Content-Type: application/json' \
  -d '{
    "skill": "renewal_risk_scorer",
    "payload": {"Account Name": "Alpha", "Renewal Date": "2027-01-01"}
  }'
```
