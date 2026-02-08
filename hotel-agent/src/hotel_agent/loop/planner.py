from __future__ import annotations

from hotel_agent.api.schemas import HotelResult, SearchRequest, SearchResponse
from hotel_agent.loop.router import get_connector
from hotel_agent.loop.types import SearchCriteria


def plan_and_search(request: SearchRequest) -> SearchResponse:
    criteria: SearchCriteria = {
        "prompt": request.prompt,
        "constraints": request.constraints,
    }
    connector = get_connector()
    raw_results = connector.search(criteria)
    results = [HotelResult(**item) for item in raw_results]
    return SearchResponse(
        query={"prompt": request.prompt, "constraints": request.constraints},
        results=results,
        questions=[],
        explanation=None,
        meta={"source": "stub_tripadvisor", "took_ms": 1},
    )
