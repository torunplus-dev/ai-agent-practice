from __future__ import annotations

from hotel_agent.connectors.base import HotelSearchConnector
from hotel_agent.loop.types import SearchCriteria


class TripadvisorConnector(HotelSearchConnector):
    def search(self, criteria: SearchCriteria) -> list[dict]:
        _ = criteria
        # TODO: Replace with actual Tripadvisor API integration.
        return [
            {
                "name": "Hotel Sakura",
                "hotel_id": 101,
                "price": {"amount": 180, "currency": "USD"},
                "rating": 4.5,
                "review_count": 1240,
                "highlights": ["駅近", "朝食付き"],
                "booking_url": "https://example.com/hotel-sakura",
            },
            {
                "name": "River View Inn",
                "hotel_id": 202,
                "price": {"amount": 140, "currency": "USD"},
                "rating": 4.1,
                "review_count": 860,
                "highlights": ["リバービュー", "静かな立地"],
                "booking_url": "https://example.com/river-view-inn",
            },
            {
                "name": "City Lights Hotel",
                "hotel_id": 303,
                "price": {"amount": 210, "currency": "USD"},
                "rating": 4.7,
                "review_count": 1900,
                "highlights": ["夜景", "大浴場"],
                "booking_url": "https://example.com/city-lights-hotel",
            },
        ]
