# pylint: disable=missing-function-docstring missing-module-docstring

from os import path
from unittest import mock

from vcr import VCR

from app import main
from app.settings import settings as app_settings

tests_vcr = VCR(
    cassette_library_dir=path.join(path.dirname(__file__), "fixtures"),
    path_transformer=lambda path: path + ".yaml",
    ignore_hosts=["testserver"],
)


@tests_vcr.use_cassette()
def test_get_tops_with_from_date(client):
    response = client.get("/tops/", params={"from_date": "2023-05-11"})
    assert response.status_code == 200
    assert len(response.json()) == app_settings.DEFAULT_LIMIT


@tests_vcr.use_cassette()
def test_get_tops_with_all_languages(client):
    response = client.get("/tops/")
    assert response.status_code == 200
    assert len(response.json()) == app_settings.DEFAULT_LIMIT


@tests_vcr.use_cassette()
def test_get_tops_with_specific_language(client):
    response = client.get("/tops/", params={"language": "Python"})
    assert response.status_code == 200
    assert len(response.json()) == app_settings.DEFAULT_LIMIT


@tests_vcr.use_cassette()
def test_get_tops_with_specific_limit_50(client):
    """
    Unfortunatelly can't use pytest.parametrize, given that
    VCR uses the test function's name to save the cassette.
    """
    limit = 50
    response = client.get("/tops/", params={"limit": str(limit)})
    assert response.status_code == 200
    assert len(response.json()) == limit


@tests_vcr.use_cassette()
def test_get_tops_with_specific_limit_100(client):
    limit = 100
    response = client.get("/tops/", params={"limit": str(limit)})
    assert response.status_code == 200
    assert len(response.json()) == limit


@tests_vcr.use_cassette()
def test_get_tops_with_invalid_limits(client):
    response = client.get("/tops/", params={"limit": "123"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "enum",
                "loc": ["query", "limit"],
                "msg": "Input should be 10, 50 or 100",
                "input": "123",
                "ctx": {"expected": "10, 50 or 100"},
            }
        ]
    }


@tests_vcr.use_cassette()
def test_get_tops_with_invalid_from_date(client):
    response = client.get("/tops/", params={"from_date": "XXXX-XX-XX"})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "date_from_datetime_parsing",
                "loc": ["query", "from_date"],
                "msg": "Input should be a valid date or datetime, invalid character in year",
                "input": "XXXX-XX-XX",
                "ctx": {"error": "invalid character in year"},
            }
        ]
    }


@tests_vcr.use_cassette()
def test_get_tops_with_rate_limit_exceeded(client):
    with mock.patch.object(main.logger, "exception") as mock_logger_exception:
        response = client.get("/tops/")
        mock_logger_exception.assert_called_once_with("Unexpected exception.")

    assert response.status_code == 500
    assert response.json() == {
        "detail": "It's been an internal server error. Please contact the service's administrator."
    }


@mock.patch("app.crud.get_tops")
def test_get_tops_with_crud_exception(mock_crud_get_tops, client):
    mock_crud_get_tops.side_effect = Exception("Something Nasty Happened.")

    with mock.patch.object(main.logger, "exception") as mock_logger_exception:
        response = client.get("/tops/")
        mock_logger_exception.assert_called_once_with("Unexpected exception.")

    assert response.status_code == 500
    assert response.json() == {
        "detail": "It's been an internal server error. Please contact the service's administrator."
    }
