import os
import httpx

Product_SERVICE_HOST_URL = 'http://localhost:8000/api/v1/products/'
url = os.environ.get('Product_SERVICE_HOST_URL') or Product_SERVICE_HOST_URL

def is_product_present(product_id: int):
    r = httpx.get(f'{url}{product_id}')
    return True if r.status_code == 200 else False
