import requests

from cryptography.fernet import Fernet

fer = Fernet.generate_key()
fer = b'0WjX2UCETXhIh6RoLHoErblFt0L_I7CAaUHyEi5GxmE='
print(requests.get('http://127.0.0.1:8081/wrapped-key/'+fer.decode()).content)

