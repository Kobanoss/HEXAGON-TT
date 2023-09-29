from fastapi import FastAPI

from src.argparser import parser
from src.models import Data, Request
from src.utils import Build_in_log

is_udp_server: bool = parser.parse_args().mode == 'UDPS'

server_host = "127.0.0.1"
server_port = parser.parse_args().sp

web_port = parser.parse_args().wp
app: FastAPI = FastAPI()

data_sent_logger: Build_in_log = Build_in_log()
data_received_logger: Build_in_log = Build_in_log()

from src.sender import send_data
from src.routes import router

app.include_router(router)

from src.server import Receiver

receiver_thread = Receiver(server_host, server_port)


@app.on_event("startup")
async def on_startup():
    receiver_thread.start()


@app.on_event("shutdown")
async def on_shutdown():
    receiver_thread.stop_server()
    receiver_thread.join(1)
