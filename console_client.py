from pprint import pprint
import requests

data = {
    # 'name':'Корова',
    # 'name': "Лошадь",
    # 'name': "Кошка",
    'name': "Собака",
}

url = 'http://127.0.0.1:8000/api/categories/'

print('################get#######################')

response = requests.get(url, timeout=5)
# assert response.status_code == 200
print(response.status_code)
# pprint(response.json())

print('################options#######################')

response = requests.options(url, timeout=5)
# assert response.status_code == 200
print(response.status_code)
# pprint(response.json())

print('################post#######################')

response = requests.post(url, data=data, timeout=5)
# assert response.status_code == 201
print(response.status_code)
pprint(response.json())

print('#################put######################')

response = requests.put(url, json=data, timeout=5)
# assert response.status_code == 200
print(response.status_code)
pprint(response.json())

print('#################patch######################')
response = requests.patch(url, json=data, timeout=5)
# assert response.status_code == 200
print(response.status_code)
pprint(response.json())

print('#################head######################')
url = 'http://127.0.0.1:8000/api/categories/1'

response = requests.head(url, timeout=5)
# assert response.status_code == 301
print(response.status_code)
print(response.headers)

print('#################delete######################')
# pylint: disable=W0622 redefined-builtin
if response.text:
    my_id = response.json()['id']
    url = f'http://127.0.0.1:8000/api/categories/{my_id}'
    response = requests.delete(url, timeout=5)
    # assert response.status_code == 204
    print(response.status_code)
else:
    print("Нет содержимого в ответе")
