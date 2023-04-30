import requests
import pytest
import json


class TestRegistration:

    def test_200(self):
        response = requests.get("http://127.0.0.1:8000/api/books/")
        assert response.status_code == 200
        print(response.text)

    def test_create(self):
        title_json = {
            "title": "Fasxdds",
            "description": "Tax",
            "author": "1"
        }
        response = requests.post(
            "http://127.0.0.1:8000/api/books/", json=title_json)
        assert response.status_code == 201
        print(response.text)
