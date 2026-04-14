import requests
from models import User

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def test_validate_users_with_pydantic():
    response = requests.get(BASE_URL)

    # Step 1: Basic check
    assert response.status_code == 200

    data = response.json()

    # Step 2: Validate each user using Pydantic
    users = []
    for user in data:
        validated_user = User(**user)  # validation happens here
        users.append(validated_user)

    # Step 3: Assertions
    assert len(users) > 0
    assert isinstance(users[0].email, str)