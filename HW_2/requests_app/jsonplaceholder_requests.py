"""
Task 2-6
Example code demonstrating HTTP requests using urllib and requests libraries.
"""
import json
import urllib.parse
import urllib.request

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def urllib_example():
    """Demonstrates HTTP requests using urllib."""
    print("=== URLLIB EXAMPLES ===")

    # GET request
    with urllib.request.urlopen(f"{BASE_URL}/posts/1") as response:
        data = json.loads(response.read().decode("utf-8"))
        print("GET /posts/1:", data)

    # POST request
    post_data = json.dumps({"title": "foo", "body": "bar", "userId": 1}).encode("utf-8")
    req = urllib.request.Request(
        f"{BASE_URL}/posts",
        data=post_data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode("utf-8"))
        print("POST /posts:", data)


def requests_example():
    """Demonstrates HTTP requests using requests."""
    print("\n=== REQUESTS EXAMPLES ===")

    # GET request
    response = requests.get(f"{BASE_URL}/posts/1")
    print("GET /posts/1:", response.json())

    # POST request
    response = requests.post(
        f"{BASE_URL}/posts", json={"title": "foo", "body": "bar", "userId": 1}
    )
    print("POST /posts:", response.json())

    # PUT request
    response = requests.put(
        f"{BASE_URL}/posts/1",
        json={"id": 1, "title": "updated", "body": "content", "userId": 1},
    )
    print("PUT /posts/1:", response.json())

    # DELETE request
    response = requests.delete(f"{BASE_URL}/posts/1")
    print("DELETE /posts/1:", response.status_code)


if __name__ == "__main__":
    urllib_example()
    requests_example()
