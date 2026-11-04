"""Talks to the AI model over HTTP, asynchronously, with a timeout."""
import httpx

AI_URL = "http://localhost:9000/classify"   # Part 06 moves this into configuration
AI_TIMEOUT_SECONDS = 3.0


async def ask_ai(complaint: str) -> dict:
    async with httpx.AsyncClient(timeout=AI_TIMEOUT_SECONDS) as client:
        response = await client.post(AI_URL, json={"complaint": complaint})
        response.raise_for_status()
        return response.json()
