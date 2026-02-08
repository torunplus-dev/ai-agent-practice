from __future__ import annotations

from typing import Any, TypedDict


class SearchCriteria(TypedDict):
    prompt: str
    constraints: dict[str, Any] | None
