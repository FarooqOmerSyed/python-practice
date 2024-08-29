import requests

# Initialize the cache outside the function
cached = {}

def get_data(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"

    if url in cached:
        return cached[url]
    else:
        resp = requests.get(url)
        data = resp.json()
        cached[url] = data  # Store the data in the cache
        return data  # Return the data

# Example usage
data = get_data(6)
print(data)
