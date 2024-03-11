from pydantic import BaseModel


class SItemAdd(BaseModel):
    name: str
    price: float | None = None


class SItem(SItemAdd):
    id: int

