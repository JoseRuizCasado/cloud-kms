import uvicorn
import pandas as pd
from fastapi import FastAPI
from cryptography.fernet import Fernet
from pydantic import BaseModel
import base64
import numpy as np


class DEK(BaseModel):
    dek_str: str


app = FastAPI()


@app.get("/wrapped-key/{dek_str}")
def get_wrapped_key(dek_str: str):
    dek = dek_str.encode()
    bd = pd.read_csv('bd.csv')
    selected_kek = ""
    if len(bd) > 0:
        keks = np.unique(bd['KEK'].tolist())
        for kek in keks:
            consulta = bd[bd['KEK'] == kek]
            print(consulta)
            if len(consulta) < 4:
                selected_kek = str(kek).encode()
                break

        if not selected_kek:
            selected_kek = Fernet.generate_key()

    else:
        selected_kek = Fernet.generate_key()

    fernet = Fernet(selected_kek)
    new_dek = fernet.encrypt(dek)
    d = {'KEK': [selected_kek.decode()], 'DEK': [new_dek.decode()]}
    df = pd.DataFrame(data=d)
    df.to_csv('bd.csv', mode='a', header=False)
    return {"DEK": new_dek}


# def get_wrapped_key(dek_str: str):
#     dek = dek_str.encode()
#     bd = pd.read_csv('bd.csv')
#     if len(bd) > 0:
#         keks = np.unique(bd['KEK'].tolist())
#         selected_kek = ""
#         for kek in keks:
#             consulta = bd[bd['KEK'] == kek]
#             if (len(consulta) < 2) and str(dek)==consulta['DEK'].values[0]:
#                 selected_kek = kek
#                 break
#         if not selected_kek:
#             fer1 = Fernet.generate_key()
#             fer2 = Fernet.generate_key()
#             d = {'KEK': [fer1], 'DEK': [fer2]}
#             df = pd.DataFrame(data=d)
#             bd.append(df)
#             selected_kek = fer2
#             df.to_csv('bd.csv', mode='a', header=False)
#             pass
#     else:
#         # Crear KEK
#         fer1 = Fernet.generate_key()
#         fer2 = Fernet.generate_key()
#         d = {'KEK': [fer1], 'DEK': [fer2]}
#         df = pd.DataFrame(data=d)
#         bd.append(df)
#         selected_kek = fer2
#         df.to_csv('bd.csv', mode='a', header=False)
#         pass
#
#     return {"hello world": selected_kek}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
