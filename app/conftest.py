import pytest
import mock
from httpx import Request, Response


@pytest.fixture(scope="session")
def mocking():
    """Patch all requests."""
    return True


@pytest.fixture()
def response():
    def fabric(status_code=200, request=None, **kwargs):
        if request is None:
            request = Request("GET", "/")
        return Response(status_code, request=request, **kwargs)

    return fabric


@pytest.fixture(autouse=True)
def httpx(response, mocking):
    if not mocking:
        yield None
        return

    with mock.patch("httpx.Client.send") as mocked:
        mocked.return_value = response(text="httpx")
        yield mocked


@pytest.fixture
def backend():
    from .utils import BackendConnector
    yield BackendConnector()
