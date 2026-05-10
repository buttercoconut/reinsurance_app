from fastapi import FastAPI
from .contracts import api as contracts_api

app = FastAPI(title="Reinsurance Contract API")

app.include_router(contracts_api.router)

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Reinsurance Contract API"}
