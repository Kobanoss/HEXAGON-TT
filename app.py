
from src import app, web_port

if __name__ == '__main__':

    import uvicorn

    uvicorn.run(f'src:app', host='127.0.0.1', port=web_port)