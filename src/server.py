import asyncio
import re
import threading
import typing
from struct import unpack

from src import data_received_logger, is_udp_server


def _encode(data: bytes):
    msg = {"int_value": None, "string": None, "short_value": None}

    if is_udp_server:
        msg["int_value"], msg["short_value"], raw_str = unpack("<ih10s", data)
    else:
        msg["short_value"], raw_str, msg["int_value"] = unpack(">h10si", data)

    msg["string"] = re.sub(r'[\x00-\x1f]', '', raw_str.decode("utf-8"))
    data_received_logger.add(msg)

    return msg


class Receiver(threading.Thread):
    def __init__(self, host: str, port: int) -> None:
        super(Receiver, self).__init__()
        self.__host = host
        self.__port = port
        self.__main_loop = None

    def stop_server(self) -> None:
        self.__main_loop.stop()

    def run(self) -> None:
        class Handler(asyncio.DatagramProtocol if is_udp_server else asyncio.Protocol):
            def __init__(self) -> None:
                super().__init__()

            def connection_made(self, transport) -> None:
                self.transport = transport

            def data_received(self, data) -> None:
                print(f"[TCP] Received message: {_encode(data)}")
                self.transport.close()

            def datagram_received(self, data, _) -> None:
                print(f"[UDP] Received message: {_encode(data)}")

        async def tcp_server() -> None:
            inner_loop = asyncio.get_event_loop()
            server = await inner_loop.create_server(
                lambda: Handler(),
                self.__host, self.__port)

            async with server:
                await server.serve_forever()

        async def udp_server():
            inner_loop = asyncio.get_event_loop()
            asyncio.set_event_loop(inner_loop)

            await loop.create_datagram_endpoint(Handler, local_addr=(self.__host, self.__port))

        loop = asyncio.new_event_loop()
        self.__main_loop = loop

        if is_udp_server:

            loop.run_until_complete(udp_server())
        else:
            loop.run_until_complete(tcp_server())

        loop.run_forever()
