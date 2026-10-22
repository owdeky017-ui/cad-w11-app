from typing import Optional
from pydantic import BaseModel

# Base schema with common attributes
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None

# Schema for creating a new item
class ItemCreate(ItemBase):
    pass

# Schema for reading/returning an item (includes id)
class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
