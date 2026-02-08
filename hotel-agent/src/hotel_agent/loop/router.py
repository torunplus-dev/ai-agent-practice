from hotel_agent.connectors.base import HotelSearchConnector
from hotel_agent.connectors.tripadvisor import TripadvisorConnector


def get_connector() -> HotelSearchConnector:
    return TripadvisorConnector()
