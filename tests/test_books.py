import pytest

@pytest.mark.smoke
def test_get_all_books_returns_200(books_client):
    response = books_client.get_all_books()
    assert response.status_code == 200

@pytest.mark.smoke
def test_get_all_books_returns_a_list(books_client):
    response = books_client.get_all_books()
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0

@pytest.mark.smoke
def test_get_single_book_returns_matching_id(books_client):
    response = books_client.get_book_by_id(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1