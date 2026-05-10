from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/contracts", tags=["contracts"])

@router.post("/", response_model=schemas.Contract, status_code=status.HTTP_201_CREATED)
async def create_contract(contract_in: schemas.ContractCreate, db: Session = Depends(get_db)):
    contract = models.Contract(**contract_in.dict())
    db.add(contract)
    db.commit()
    db.refresh(contract)
    return contract

@router.get("/", response_model=List[schemas.Contract])
async def list_contracts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    contracts = db.query(models.Contract).offset(skip).limit(limit).all()
    return contracts
