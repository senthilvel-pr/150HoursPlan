import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

for user in data[:3]:
    print("\nUser Data:")
    print("Name:", user["name"])
    print("Email:", user["email"])
