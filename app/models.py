from pydantic import BaseModel


class HostIn(BaseModel):
    hostname: str
    key: str
    value: str

class HostOut(HostIn):
    received: str = "OK"
