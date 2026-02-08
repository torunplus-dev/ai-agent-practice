from __future__ import annotations

from typing import Protocol

from hotel_agent.loop.types import SearchCriteria


class HotelSearchConnector(Protocol):
    def search(self, criteria: SearchCriteria) -> list[dict]:
        """Search hotels based on criteria."""
