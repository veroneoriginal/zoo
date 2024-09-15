# from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth

# data = {
#     # 'name':'Корова',
#     # 'name': "Лошадь",
#     # 'name': "Кошка",
#     # 'name': "Собака",
# }

url = 'http://127.0.0.1:8000/api/viewsets/categories/'

print('################get#######################')
response = requests.get(url, auth=HTTPBasicAuth('admin', 'qwerty'),
                            timeout=5)
assert response.status_code == 200, response.status_code
print(response.status_code)
# pprint(response.json())

# print('################options#######################')
# response = requests.options(url, timeout=5)
# # assert response.status_code == 200
# print(response.status_code)
# # pprint(response.json())

# print('#################put######################')
# response = requests.put(url, json=data, timeout=5)
# # assert response.status_code == 200
# print(response.status_code)
# pprint(response.json())
#
# print('#################patch######################')
# response = requests.patch(url, json=data, timeout=5)
# # assert response.status_code == 200
# print(response.status_code)
# pprint(response.json())
#
# print('#################head######################')
# url_1 = 'http://127.0.0.1:8000/api/categories/1'

# response = requests.head(url=url_1, timeout=5)
# # assert response.status_code == 301
# print(response.status_code)
# print(response.headers)
#
# print('################post#######################')
# response = requests.post(url, data=data, timeout=5)
# # assert response.status_code == 201
# print(response.status_code)
# pprint(response.json())
# print()
#
# print('#################delete######################')
# my_id = response.json()["id"]
# print("my_id", my_id)
# url = f'http://127.0.0.1:8000/api/categories/{my_id}'
# response = requests.delete(url, timeout=5)
# # assert response.status_code == 204
# print(response.status_code)
