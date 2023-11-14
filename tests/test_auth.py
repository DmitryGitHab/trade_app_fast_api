import pytest
from sqlalchemy import insert, select

from src.auth.models import role
from tests.conftest import client, async_session_maker


# async def test_add_role():
#     # assert 1 == 1
#     async with async_session_maker() as session:
#         stmt = insert(role).values(id=15, name="admin", permissions=None)
#         await session.execute(stmt)
#         await session.commit()
#
#         query = select(role)
#         result = await session.execute(query)
#         # print(result.all())
#         # assert result.all() == [(13, 'admin', None)], "Роль не добавилась"
#         assert result.all() == [(15, 'admin', 'null')], "Роль не добавилась"

# def test_register():
#     response = client.post("/auth/register", json={
#         "email": "string",
#         "password": "string",
#         "is_active": True,
#         "is_superuser": False,
#         "is_verified": False,
#         "username": "string",
#         "role_id": 1
#     })
#
#     assert response.status_code == 201
