from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class ContractBase(BaseModel):
    reinsurer_name: str
    primary_insurer_name: str
    effective_date: date
    expiry_date: date
    premium: float
    risk_limit: float

class ContractCreate(ContractBase):
    pass

class Contract(ContractBase):
    id: int
    status: str

    class Config:
        orm_mode = True
