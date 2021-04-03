import uvicorn
import pandas as pd
from fastapi import FastAPI
from cryptography.fernet import Fernet
from pydantic import BaseModel
import numpy as np


class DEK(BaseModel):
    dek_str: str


app = FastAPI()


@app.get("/wrapped-key/{dek_str}")
def get_wrapped_key(dek_str: str):
    dek = dek_str.encode()
    bd = pd.read_csv('bd.csv')
    if len(bd) > 0:
        keks = np.unique(bd['KEK'].tolist())
        selected_kek = ""
        for kek in keks:
            if len(bd[bd['KEK'] == kek]) < 2:
                selected_kek = kek
                break
        if not selected_kek:
            # Crear KEK
            pass
    else:
        # Crear KEK
        pass

    return {"hello world": selected_kek}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
