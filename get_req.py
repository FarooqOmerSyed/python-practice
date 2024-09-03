import requests
import json

def get_data(id):
    url = f'https://jsonplaceholder.typicode.com/posts/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {}

if __name__ == '__main__':
    all_data = []
    for x in range(1, 6):
        resp = get_data(x)
        all_data.append(resp)
    
    with open('data.json', 'w') as file:
        json.dump(all_data, file, indent=4)
