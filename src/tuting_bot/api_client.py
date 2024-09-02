import logging
from typing import Optional

import aiohttp


class ApiClient:
    """TODO: API client for the backend of the accounting bot."""

    """Maybe it's better to use gRPC instead of REST, think about it later."""

    def __init__(self, token: str):
        self.token = token
        self.base_url = f'golang/api/v1/'

    async def get_updates(self) -> Optional[dict]:
        return await self._make_request('getUpdates')

    async def _make_request(self, method: str) -> Optional[dict]:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'{self.base_url}/{method}') as response:
                    response.raise_for_status()
                    return await response.json()
            except aiohttp.ClientError as e:
                logging.error(f"API request failed: {e}")
                return None
