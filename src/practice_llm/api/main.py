"""FastAPI application entry point."""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="practice-llm",
    version="0.1.0",
    description="A learning-focused decoder-only LLM chat application.",
)


class HealthResponse(BaseModel):
    """Response returned when the service is available."""

    status: Literal["ok"]


@app.get("/health", response_model=HealthResponse, tags=["service"])
def health() -> HealthResponse:
    """Report that the HTTP service is ready to receive requests."""
    return HealthResponse(status="ok")
