from pydantic import BaseModel


class Receiver(BaseModel):
    ipv4: str
    port: int


class Data(BaseModel):
    int_value: int
    string: str
    short_value: int


class Request(BaseModel):
    receiver: Receiver
    data: Data
