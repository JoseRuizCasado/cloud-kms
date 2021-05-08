import requests
import json
from cryptography.fernet import Fernet

fer = b'gAAAAABgagQZEfiFmW_BOjFOdlKr7DKH-hwKI94WamiwrPua4vSTmcahNmqeEJmapO_gNJTC3tS72uS5XIJDTG96Ku894RR-Eg_ik6SFM9J6lSbg0OsQBtxVasJCH5v-40tJW-mCQy49'
response = requests.get('http://127.0.0.1:8081/get-key/'+fer.decode()).content.decode()
json_res = json.loads(response)
print(json_res['DEK'].encode())
