# import pytest
# from aiohttp import web
# from aiohttp.test_utils import TestClient, TestServer

# from tuting_bot.api_client import ApiClient

# pytest_plugins = ['pytest_aiohttp']

# @pytest.fixture
# async def api_server(aiohttp_client: TestClient) -> TestServer:
#     async def mock_updates(request: web.Request) -> web.Response:
#         return web.json_response({"ok": True, "result": [{"update_id": 1}]})

#     app = web.Application()
#     app.router.add_get('/botTEST_TOKEN/getUpdates', mock_updates)
#     return await aiohttp_client(TestServer(app))

# @pytest.fixture
# async def api_client(api_server: TestServer):
#     client = ApiClient("TEST_TOKEN")
#     client.base_url = api_server.make_url('')
#     return client

# @pytest.mark.asyncio
# async def test_get_updates(api_client: ApiClient, api_server: TestServer) -> None:
#     api_client.base_url = api_server.make_url('')

#     updates = await api_client.get_updates()
#     assert updates == {"ok": True, "result": [{"update_id": 1}]}  # noqa: S101

# @pytest.mark.asyncio
# async def test_make_request_error(api_client: ApiClient, api_server: TestServer) -> None:
#     api_client.base_url = api_server.make_url('/non-existent')

#     result = await api_client._make_request('getUpdates')
#     assert result is None  # noqa: S101
