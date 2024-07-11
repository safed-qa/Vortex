import pytest
import requests
from allure import step

BASE_URL = "https://reqres.in/api"

@pytest.fixture
def user_data():
    return {
        "name": "kesha",
        "job": "good guy"
    }

@pytest.fixture
def updated_user_data():
    return {
        "name": "gosha",
        "job": "Dementor helper"
    }

@pytest.fixture
def created_user_id(user_data):
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code == 201
    return response.json()["id"]

@step("Get single user")
def test_get_single_user():
    user_id = 2
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    with step("Check status code"):
        assert response.status_code == 200
    with step("Check user data"):
        user = response.json()["data"]
        assert user["id"] == user_id
        assert user["email"] == "janet.weaver@reqres.in"
        assert user["first_name"] == "Janet"
        assert user["last_name"] == "Weaver"

@step("Create user")
def test_create_user(user_data):
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    with step("Check status code"):
        assert response.status_code == 201
    with step("Check user data"):
        user = response.json()
        assert user["name"] == user_data["name"]
        assert user["job"] == user_data["job"]
        assert "id" in user
        assert "createdAt" in user

@step("Update user")
def test_update_user(created_user_id, updated_user_data):
    response = requests.put(f"{BASE_URL}/users/{created_user_id}", json=updated_user_data)
    with step("Check status code"):
        assert response.status_code == 200
    with step("Check updated user data"):
        user = response.json()
        assert user["name"] == updated_user_data["name"]
        assert user["job"] == updated_user_data["job"]
        assert "updatedAt" in user