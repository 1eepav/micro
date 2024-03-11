from sqlalchemy import select
from database import ItemOrm, new_session
from schemas import SItemAdd, SItem


class ItemRepository:
    @classmethod
    async def add_item(cls, data: SItemAdd) -> int:
        async with new_session() as session:
            item_dict = data.model_dump()

            item = ItemOrm(**item_dict)
            session.add(item)
            await session.flush()
            await session.commit()
            return item.id

    @classmethod
    async def read_by_id(cls, data: SItem) -> list[SItem]:
        async with new_session() as session:
            item_dict = data.model_dump()
            item = ItemOrm(**item_dict)
            session.add(item)
            await session.query(data).get(id)
            await session.commit()
            # item = session.query(ItemOrm).get(id)


    @classmethod
    async def find_all(cls) -> list[SItem]:
        async with new_session() as session:
            query = select(ItemOrm)
            result = await session.execute(query)
            item_models = result.scalars().all()
            return item_models

    # @classmethod
    # async def update_item(cls):

    # @classmethod
    # async def find_all(cls) -> list[SItem]:
    #     async with new_session() as session:
    #         query = select(ItemOrm)
    #         result = await session.execute(query)
    #         item_models = result.scalars().one()
    #         # items = [SItem.model_validate(item_models) for item_models in item_models]
    #         return item_models

    # @classmethod
    # async def delete_item(cls) -> list[SItem]:
    #     async with new_session() as session:
    #         query = select(ItemOrm)
    #         result = await session.execute(query)
    #         item_models =
