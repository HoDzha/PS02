# Задание 2: Параметры запрос
# 1. Используйте API, который позволяет фильтрацию данных через URL-параметры \
# (например, https://jsonplaceholder.typicode.com/posts).
# 2. Отправьте GET-запрос с параметром `userId`, равным `1`.
# 3. Распечатайте полученные записи.

import requests
import pprint
url = 'https://jsonplaceholder.typicode.com/posts'
params = {
    'userId' : '1'
}
response = requests.get(url,params=params)
response_json = response.json()
pprint.pprint(response_json)




