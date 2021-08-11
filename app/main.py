import logging
import time
import uuid

from fastapi import FastAPI, Request
from fastapi.logger import logger

logging.basicConfig(level=logging.DEBUG)
gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers
if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)


app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    idem = uuid.uuid4()
    # logger.info(f"rid={idem} start request path={request.url.path}")
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"request_id={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

    return response


# sample call
@app.get("/")
async def root():
    logger.info("Root called")
    return {"root": "root"}
