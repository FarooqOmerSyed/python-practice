import requests
import pytest

# Define URL
url = 'https://jsonplaceholder.typicode.com'

# Sample test cases 
test_cases = [
    (1,200), # valid post ID
    (2,200), #valid post ID
    (100, 404), #invalid post ID #fail
    ('abc', 404), #invalid request
    ('None', 404), #None as ID
]

@pytest.mark.parametrize("post_id, expected_status", test_cases)
def test_get_post(post_id, expected_status):
    response = requests.get(f"{url}/posts/{post_id}")
    assert response.status_code == expected_status

if __name__ == '__main__':
    pytest.main()

# pytest -v test_get_post.py