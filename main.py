import uvicorn
from fastapi import FastAPI
from cryptography.fernet import Fernet
from pydantic import BaseModel


class DEK(BaseModel):
    dek_str: str


app = FastAPI()


@app.get("/wrapped-key/{dek_str}")
def get_wrapped_key(dek_str: str):
    dek = dek_str.encode()

    return {"hello world": dek_str}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
