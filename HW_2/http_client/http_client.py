"""Task 2-8: HTTP client using match-case for method dispatch"""

import json

import requests


def http_client(url: str, method: str, data: dict = None):
    """
    HTTP client using match-case for method dispatch
    """
    method = method.upper()
    try:
        match method:
            case "GET":
                resp = requests.get(url, params=data)
            case "POST":
                resp = requests.post(url, json=data)
            case "PUT":
                resp = requests.put(url, json=data)
            case "DELETE":
                resp = requests.delete(url, json=data)
            case _:
                print(f"Unsupported method: {method}")
                return

        # Print status code
        print(f"Status code: {resp.status_code}")

        # Print headers
        print("Headers:")
        for key, value in resp.headers.items():
            print(f"  {key}: {value}")

        # Print body
        print("\nBody:")
        try:
            print(json.dumps(resp.json(), indent=2))
        except ValueError:
            print(resp.text)

    except requests.RequestException as exc:
        print(f"HTTP request failed: {exc}")


if __name__ == "__main__":
    # Example GET request
    url = "https://jsonplaceholder.typicode.com/posts/1"
    method = "GET"
    http_client(url, method)
