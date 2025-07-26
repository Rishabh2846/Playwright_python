import requests
import pytest

def test_get_method():
    url = "https://practice.expandtesting.com/notes/api/health-check"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json().get("message") == "Notes API is Running"

def test_post_user_registration():
    url = "https://practice.expandtesting.com/notes/api/users/register"
    payload = {
        "name": "testiuyghgkjbbb",
        "email": "testnkjnkjhg@tyh.com",
        "password": "Password12335345435"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 409:
        assert response.json().get("message") == "An account already exists with the same email address"
    elif response.status_code == 201:
        assert response.json().get("message") == "User account created successfully"
    else:
        pytest.fail(f"Unexpected status code: {response.status_code}")
