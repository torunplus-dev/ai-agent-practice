from fastapi import APIRouter

from hotel_agent.api.schemas import SearchRequest, SearchResponse
from hotel_agent.loop.planner import plan_and_search

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/search", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    return plan_and_search(request)
