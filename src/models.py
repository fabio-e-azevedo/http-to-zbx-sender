from pydantic import BaseModel


class JsonIn(BaseModel):
    hostname: str
    key: str
    value: str

class JsonOut(JsonIn):
    received: str = "OK"

