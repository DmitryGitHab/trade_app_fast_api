import json
import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
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

@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"


@router.get("/{id}, response_model=List[OperationCreate]")
async def get_id(id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.id == id)
        result = await session.execute(query)
        # return result.mappings().all()
        return {
            'status': 'succes',
            # 'data': result.all(),
            'data': result.mappings().all(),
            'details': None,
        }
    except Exception:
        return {
            'status': 'error',
            'data': None,
            'details': None,
        }


# @router.get("/, response_model=List[OperationCreate]"")
@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        # return result.mappings().all()
        return {
            'status': 'succes',
            # 'data': result.all(),
            'data': result.mappings().all(),
            'details': None,
        }
    except Exception:
        raise HTTPException(status_coe=500, detail={
            'status': 'error',
            'data': None,
            'details': None,
        })



@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(operation).values(**new_operation.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception:
        raise HTTPException(status_coe=500, detail={
            'status': 'error',
            'data': None,
            'details': None,
        })

