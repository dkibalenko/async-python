import time, asyncio, logging, threading

from fastapi import FastAPI

# basic config. attach logger to Uvicorn’s logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
# now will print to the console
log = logging.getLogger(__name__)


app = FastAPI(docs_url=None)

hotels = [
    {"id": 1, "title": "Berlin", "name": "berlin"},
    {"id": 2, "title": "Amsterdam", "name": "amsterdam"}
]


@app.get("/sync/{id}")
def sync_func(id: int):
    """Sync endpoints block the event loop, so Starlette/Uvicorn offload them to a threadpool"""
    log.info(f"Sync. THREADS: {threading.active_count()}")
    start = time.time()
    time.sleep(3)  # blocking sleep
    log.info(f"Sync. Finished {id} in: {time.time() - start:.2f}s")


@app.get("/async/{id}")
async def async_func(id: int):
    """Async endpoints never spawn threads for I/O.
    They run entirely inside the event loop."""
    # async endpoints do NOT use threads for request handling
    log.info(f"Async. THREADS: {threading.active_count()}")
    start = time.time()
    await asyncio.sleep(3)  # mimic db query, cache, api..
    log.info(f"Async. Finished {id} in: {time.time() - start:.2f}s")
