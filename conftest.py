import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app as main_app


@pytest.fixture(scope="function")
def app():
    _app = main_app
    yield _app


@pytest.fixture(scope="function")
def client(app: FastAPI):
    with TestClient(app) as client:
        yield client
