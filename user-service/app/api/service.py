import os
import httpx

User_SERVICE_HOST_URL = 'http://localhost:8000/api/v1/users/'
url = os.environ.get('User_SERVICE_HOST_URL') or User_SERVICE_HOST_URL

def is_user_present(user_id: int):
    r = httpx.get(f'{url}{user_id}')
    return True if r.status_code == 200 else False
