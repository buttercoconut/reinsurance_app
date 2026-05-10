from fastapi import FastAPI
from .contracts import api as contracts_api

app = FastAPI(title="Reinsurance Backend")

app.include_router(contracts_api.router)
