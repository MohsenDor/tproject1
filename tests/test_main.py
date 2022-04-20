import pytest
from httpx import AsyncClient


# @pytest.mark.anyio
# async def test_root():
#     async with AsyncClient(app=app, base_url="http://0.0.0.0:8000") as ac:
#         request_example = {"x": "string","y": 12}
#         response1 = await ac.post("/add", json=request_example)
#         response = await ac.get("/")
        

#     assert response1.status_code == 200
#     assert response1.json()=={"string": 12}
#     assert response.status_code == 200
#     assert response.json() == {"message": "Tomato"}


@pytest.mark.asyncio
async def test_xy(async_client:AsyncClient):
    request_example = {"x": "string","y": 12}
    response1 = await async_client.post("/add", json=request_example)
    assert response1.status_code == 200
    assert response1.json()=={"string": 12}

@pytest.mark.asyncio
async def test_xy1(async_client:AsyncClient):
    request_example = {"x": "string","y": 12}
    response1 = await async_client.post("/add", json=request_example)
    assert response1.status_code == 200
    assert response1.json()=={"string": 12}


@pytest.mark.asyncio
async def test_xy2(async_client:AsyncClient):
    request_example = {"x": "string","y": 12}
    response1 = await async_client.post("/add", json=request_example)
    assert response1.status_code == 200
    assert response1.json()=={"string": 12}

@pytest.mark.asyncio
async def test_xy3(async_client:AsyncClient):
    request_example = {"x": "string","y": 12}
    response1 = await async_client.post("/add", json=request_example)
    assert response1.status_code == 200
    assert response1.json()=={"string": 12}

@pytest.mark.asyncio
async def test_xy4(async_client:AsyncClient):
    request_example = {"x": "string","y": 12}
    response1 = await async_client.post("/add", json=request_example)
    assert response1.status_code == 200
    assert response1.json()=={"string": 12}