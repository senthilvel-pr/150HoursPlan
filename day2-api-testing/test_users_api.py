import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"


def test_status_code():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def test_response_is_list():
    response = requests.get(BASE_URL)
    data = response.json()
    assert isinstance(data, list)


def test_first_user_has_name():
    response = requests.get(BASE_URL)
    data = response.json()
    assert "name" in data[0]