from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    prompt: str
    constraints: dict[str, Any] | None = None
    llm: dict[str, Any] | None = None


class HotelResult(BaseModel):
    name: str
    hotel_id: int | None = None
    price: dict[str, Any] | None = None
    rating: float | None = None
    review_count: int | None = None
    highlights: list[str] = Field(default_factory=list)
    booking_url: str | None = None


class SearchResponse(BaseModel):
    query: dict[str, Any]
    results: list[HotelResult]
    questions: list[str]
    explanation: str | None = None
    meta: dict[str, Any]
