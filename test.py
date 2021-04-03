import requests

response = requests.get(url='http://0.0.0.0:8081/wrapped-key/prueba')

print(response.content)
