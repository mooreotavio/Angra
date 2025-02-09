from http import HTTPStatus

from fastapi.testclient import TestClient

from angra.app import app

client = TestClient(app)


def test_read_root_return_ok_hw():
    assert client.get('/').status_code == HTTPStatus.OK
    assert client.get('/').json() == {'message': 'OLÁ MUNDO'}
