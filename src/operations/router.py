import json

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, JSON
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate
from typing import List

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/{id}", response_model=List[OperationCreate])
async def get_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.id == id)
    result = await session.execute(query)
    return result.all()

@router.get("/", response_model=List[OperationCreate])
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
