import requests

from cryptography.fernet import Fernet

fer = Fernet.generate_key()
fer = b'tVotD02KLMfrVYvJvpsNBS5KYhGsE1za-o5RFeB9WqQ='
print(requests.get('http://127.0.0.1:8081/wrapped-key/'+fer.decode()).content)

