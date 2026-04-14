import requests
import sys
from models import User


def fetch_users(url):
    print("👉 Calling API now...")
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ API Request Failed: {e}")
        return []


def validate_users(users):
    """Validate users using Pydantic"""
    valid_users = []

    for user in users:
        try:
            validated_user = User(**user)
            valid_users.append(validated_user)
        except Exception as e:
            print(f"❌ Validation failed for user: {user.get('name', 'Unknown')}")
            print(f"Error: {e}\n")

    return valid_users

def main():
    default_url = "https://jsonplaceholder.typicode.com/users"

    user_input = input("Enter API URL (or press Enter to use default): ").strip()

    if user_input:
        url = user_input
    else:
        url = default_url

    print(f"\n📡 Fetching data from: {url}\n")

    users = fetch_users(url)

    if not users:
        print("⚠ No data received. Exiting program.")
        return
    
    valid_users = validate_users(users)

    print(f"\n✅ Total valid users: {len(valid_users)}\n")

    for user in valid_users:
        print(f"✔ {user.name} | {user.email}")


if __name__ == "__main__":
    main()

"""
def main():
    # Default API
    url = "https://jsonplaceholder.typicode.com/users"

    # Allow user to pass URL from terminal
    if len(sys.argv) > 1:
        url = sys.argv[1]

    print(f"\n📡 Fetching data from: {url}\n")

    users = fetch_users(url)
    valid_users = validate_users(users)

    print(f"\n✅ Total valid users: {len(valid_users)}\n")

    for user in valid_users:
        print(f"✔ {user.name} | {user.email}")

"""
