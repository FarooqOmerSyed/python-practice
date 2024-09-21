import pytest
import requests

@pytest.fixture
def session():
    return requests.Session()

def test_create_post(session):
    url = 'https://jsonplaceholder.typicode.com/posts'
    post_data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = session.post(url, json=post_data)
    assert response.status_code == 201
    assert response.json()['title'] == 'foo'

def test_read_post(session):
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = session.get(url)
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_update_post(session):
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    update_data = {'id': 1, 'title': 'foo updated', 'body': 'bar updated', 'userId': 1}
    response = session.put(url, json=update_data)
    assert response.status_code == 200
    assert response.json()['title'] == 'foo updated'

def test_delete_post(session):
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = session.delete(url)
    assert response.status_code == 200
