import logging
from fastapi import FastAPI
from routes import router
import uvicorn


logging.basicConfig(
    filename="logs/logs.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s| %(message)s",
)

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3001)
