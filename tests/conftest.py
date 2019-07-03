"""Pytest setup stuff."""
import pytest

import main


@pytest.fixture(scope='function', autouse=True)
async def client(aiohttp_client):
    """Setup the aiohttp client for tests."""
    app = await main.get_app()
    return await aiohttp_client(app.app)
