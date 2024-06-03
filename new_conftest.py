import pytest
import yaml
import requests

with open("new_config.yaml", "r") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(data["address_1"], data={"username": data["username"], "password": data["password"]})
    return res1.json()["token"]

@pytest.fixture()
def find_id():
    return 96154

@pytest.fixture()
def title():
    return "Writer"

@pytest.fixture()
def description():
    return "Turgenev"

@pytest.fixture()
def content():
    return "D.A.Turgenev"

@pytest.fixture()
def find_description():
    return "Turgenev"