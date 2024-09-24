# Задание 2: Параметры запрос
# 1. Используйте API, который позволяет фильтрацию данных через URL-параметры \
# (например, https://jsonplaceholder.typicode.com/posts).
# 2. Отправьте GET-запрос с параметром `userId`, равным `1`.
# 3. Распечатайте полученные записи.

import requests
import pprint
url = 'https://jsonplaceholder.typicode.com/posts'
params = {
    'userid' : '1'
}
response = requests.get(url,params=params)
requests_json = response.json()
pprint.pprint(requests)



