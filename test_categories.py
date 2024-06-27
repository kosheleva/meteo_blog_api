from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_categories_get_all():
    response = client.get("/categories/")
    assert response.status_code == 200


# @todo: move to a "tests" folder, add more tests