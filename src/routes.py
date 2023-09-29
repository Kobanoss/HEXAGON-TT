from fastapi import APIRouter, BackgroundTasks

from src.models import Request
from src import data_sent_logger, data_received_logger, send_data

api_subpath: str = "/api/v1"

router = APIRouter()


@router.post(api_subpath + "/send")
async def data_send(request: Request, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_data, request)
    return {"status": "OK"}


@router.get(api_subpath + "/stat/received")
async def data_received():
    return {"Received": data_received_logger.get()}


@router.get(api_subpath + "/stat/sent")
async def data_sent():
    return {"Sent": data_sent_logger.get()}
