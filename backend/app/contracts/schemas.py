from pydantic import BaseModel, Field
from datetime import datetime

class ContractCreate(BaseModel):
    insurer_name: str
    reinsurer_name: str
    premium: float
    risk_limit: float
    start_date: datetime
    end_date: datetime

class ContractOut(ContractCreate):
    id: int
    status: str = Field(default="active")

    class Config:
        orm_mode = True
