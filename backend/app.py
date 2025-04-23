import yaml
from fastapi import FastAPI

from .api.visibility import router


def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

config: dict = load_config('config.yaml')

app = FastAPI()
app.include_router(router)