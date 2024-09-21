import pytest
import requests

@pytest.fixture
def session():
    return requests.Session()

@pytest.fixture
def base_url():
    return 'https://jsonplaceholder.typicode.com/posts'

def test_create_post(session, base_url):
    post_data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = session.post(base_url, json=post_data)
    assert response.status_code == 201
    assert response.json()['title'] == 'foo'

def test_read_post(session, base_url):
    response = session.get(f'{base_url}/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_update_post(session, base_url):
    update_data = {'id': 1, 'title': 'foo updated', 'body': 'bar updated', 'userId': 1}
    response = session.put(f'{base_url}/1', json=update_data)
    assert response.status_code == 200
    assert response.json()['title'] == 'foo updated'

def test_delete_post(session, base_url):
    response = session.delete(f'{base_url}/1')
    assert response.status_code == 200
