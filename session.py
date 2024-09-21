import requests

# Create a session object
session = requests.Session()

# Base URL for JSONPlaceholder
url = 'https://jsonplaceholder.typicode.com/posts'

# Create (POST)
post_data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response = session.post(url, json=post_data)
print('CREATE:', response.json())

# Read (GET)
response = session.get(url + '/1')
print('READ:', response.json())

# Update (PUT)
update_data = {
    'id': 1,
    'title': 'foo updated',
    'body': 'bar updated',
    'userId': 1
}
response = session.put(url + '/1', json=update_data)
print('UPDATE:', response.json())

# Delete (DELETE)
response = session.delete(url + '/1')
print('DELETE:', response.status_code)
