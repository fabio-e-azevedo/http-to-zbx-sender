import os
import uvicorn
from typing import List
from functools import lru_cache
from fastapi import FastAPI
from models import JsonIn, JsonOut
from zbxsender import Sender
import conf


app = FastAPI()


@lru_cache()
def get_settings():
    return conf.DevConfig()


@app.post("/alert/", response_model=JsonOut, status_code=201)
async def alert_value(host: JsonIn):
    result = JsonOut(**host.dict(), received='Faild')
    return result


if __name__ == "__main__":
    conf = get_settings()
    uvicorn.run(app, host="0.0.0.0", port=os.environ['PORT'])
