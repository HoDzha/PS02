# 1. Отправьте GET-запрос к открытому API (например, https://api.github.com)
# с параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

url = 'https://api.github.com/search/repositories'
params = {
    'q':'html'
}
response = requests.get(url,params=params)
response_json = response.json()
print(response.status_code)
pprint.pprint(response_json)




