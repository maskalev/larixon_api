import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db(transaction=True)
class TestAdvertViewSet:
    def test_list_function_returns_correct_data(self):
        response = client.get("/api/advert-list/")
        assert response.status_code == 200
        assert response.data["count"] == 2

        response = client.get("/api/advert/")
        assert response.status_code == 404

    def test_retrieve_function_returns_correct_data(self):
        response = client.get("/api/advert-list/1/")
        assert response.status_code == 404

        response = client.get("/api/advert/1/")
        assert response.status_code == 200
        assert response.data["title"] == "Title 1"
        assert response.data["description"] == "Description 1"
        assert response.data["city"] == "City 1"
        assert response.data["category"] == "Category 1"

    def test_post_method_is_not_allowed(self):
        response = client.post("/api/advert-list/")
        assert response.status_code == 405

        response = client.post("/api/advert/1/")
        assert response.status_code == 405

    def test_views_increasing(self):
        response = client.get("/api/advert/2/")
        assert response.status_code == 200
        assert response.data["views"] == 1
        response = client.get("/api/advert/2/")
        assert response.data["views"] == 2
