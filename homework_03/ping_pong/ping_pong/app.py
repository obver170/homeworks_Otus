from fastapi import FastAPI

app = FastAPI()


@app.get("/ping/", summary='Get "pong"')
def get_pong():
    """
    :return: {'message': 'pong'}
    """
    return {'message': 'pong'}
