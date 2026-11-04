"""Complaint Triage Service, Part 05: async calls to the AI."""
import httpx
from fastapi import FastAPI

from app.ai_client import AI_URL
from app.models import ComplaintIn, TriageResponse
from app.triage import ai_triage

app = FastAPI(title="Complaint Triage Service", version="1.1.0")


@app.post("/triage", response_model=TriageResponse)
async def triage(body: ComplaintIn) -> TriageResponse:
    return await ai_triage(body.complaint)


# DEMO ONLY: the blocking trap. async def, but a blocking HTTP call inside.
# We remove this endpoint in Part 06.
@app.post("/demo/blocking")
async def triage_blocking(body: ComplaintIn) -> dict:
    response = httpx.post(AI_URL, json={"complaint": body.complaint}, timeout=10)
    return response.json()
