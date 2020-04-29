import uvicorn
from functools import lru_cache
from fastapi import FastAPI
from models import HostIn, HostOut
from zbxsender import Sender
import conf


app = FastAPI()


@lru_cache()
def get_settings():
    return conf.DevConfig()


@app.post("/alert/", response_model=HostOut, status_code=201)
async def host_value(host: HostIn):
    result = HostOut(**host.dict(), received='Faild')
    return result


if __name__ == "__main__":
    conf = get_settings()
    uvicorn.run(app, host="0.0.0.0", port=conf.APP_PORT)
