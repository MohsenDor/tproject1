import asyncio
import pytest
from httpx import AsyncClient
from main import app

BASE_URL="http://0.0.0.0:8000"

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().get_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def async_client():
    async with AsyncClient(app=app, base_url=BASE_URL) as async_client:
        yield async_client

