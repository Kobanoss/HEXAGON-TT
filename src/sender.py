import asyncio
from struct import pack

import asyncio_dgram

from src import data_sent_logger, is_udp_server
from src.models import Data, Request


async def convert_data(data: Data) -> bytes:
    if not is_udp_server:
        return pack("<ih10s", data.int_value, data.short_value, data.string.encode('utf-8'))
    else:
        return pack(">h10si", data.short_value, data.string.encode('utf-8'), data.int_value)


async def send_data(request: Request) -> None:
    msg: bytes = await convert_data(request.data)

    try:
        if not is_udp_server:
            stream = await asyncio_dgram.connect((request.receiver.ipv4, request.receiver.port))

            await stream.send(msg)

            stream.close()

        else:
            _, writer = await asyncio.open_connection(
                request.receiver.ipv4, request.receiver.port)

            writer.write(msg)
            await writer.drain()

            writer.close()
            await writer.wait_closed()

    except ConnectionRefusedError as e:
        print(e)
        return

    data_sent_logger.add(dict(request))
