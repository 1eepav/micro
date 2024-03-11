from fastapi import APIRouter, Depends
from repository import ItemRepository
from schemas import SItemAdd


router = APIRouter(prefix="/items", tags=["Товары"])


@router.post("")
async def add_item(item: SItemAdd = Depends()):
    item_id = await ItemRepository.add_item(item)
    return {"data": True, "item_id": item_id}


@router.get("")
async def get_items():
    items = await ItemRepository.find_all()
    return {"items": items}


@router.get("/{id}")
async def get_item():
    item = await ItemRepository.read_by_id()
    return {"item": item}


@router.put("/{id}")
async def update_item():
    item_id = await ItemRepository.put_item()
    return {"item": item_id}
