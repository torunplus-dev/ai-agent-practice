from fastapi import FastAPI

from hotel_agent.api.routes import router

app = FastAPI(title="Hotel Agent", version="0.1.0")
app.include_router(router)
