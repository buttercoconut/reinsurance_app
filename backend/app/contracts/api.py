from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/contracts", tags=["contracts"])

@router.post("/", response_model=schemas.ContractOut)
async def create_contract(contract: schemas.ContractCreate, db: AsyncSession = Depends(get_db)):
    new_contract = models.Contract(**contract.dict())
    db.add(new_contract)
    try:
        await db.commit()
        await db.refresh(new_contract)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Contract could not be created")
    return new_contract

@router.get("/", response_model=list[schemas.ContractOut])
async def list_contracts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Contract))
    contracts = result.scalars().all()
    return contracts
