from fastapi import FastAPI

from .api.visibility import router


app = FastAPI()
app.include_router(router)