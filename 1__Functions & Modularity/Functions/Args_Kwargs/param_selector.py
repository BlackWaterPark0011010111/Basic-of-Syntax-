import requests

def build_url(base_url, endpoint, **params):
    url = f"{base_url}/{endpoint}?"
    for key, value in params.items():
        url += f"{key}={value}&"
    return url.rstrip('&')

def make_api_request(*args, **kwargs):
    base_url = kwargs.get('base_url', 'https://api.example.com')
    endpoint = kwargs.get('endpoint', 'data')
    params = kwargs.get('params', {})

    url = build_url(base_url, endpoint, **params)
    response = requests.get(url)
    return response.json()

# Example usage
response = make_api_request(base_url="https://api.openai.com", endpoint="v1/models", params={"limit": 10, "offset": 0})
print(response)


