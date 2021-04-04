import requests

from cryptography.fernet import Fernet

fer = Fernet.generate_key()
fer = b'B-nOwhZu83Jpi2ZqjnGstgb3ORJwLvTEyQc3wyT-LLE='
print(requests.get('http://127.0.0.1:8081/wrapped-key/'+fer.decode()).content)

