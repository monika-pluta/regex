import requests
URL = 'https://pl.wikipedia.org/wiki/Witaszyce'

with requests.session() as s:
    response = s.get(URL).text

print(response)