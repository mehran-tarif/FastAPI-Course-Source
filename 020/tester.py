import requests

for i in range(100):
    response = requests.get("http://localhost:8000/", headers={"accept": "application/json"})
    print(response.json())