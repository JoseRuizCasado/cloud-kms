import requests

from cryptography.fernet import Fernet

fer = Fernet.generate_key()
print(requests.get('http://127.0.0.1:8081/wrapped-key/'+fer.decode()).content)

