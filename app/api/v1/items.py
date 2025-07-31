from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_current_active_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.item import Item as ItemSchema, ItemCreate, ItemUpdate
from app.services.item_service import ItemService

router = APIRouter()

@router.post("/", response_model=ItemSchema, status_code=status.HTTP_201_CREATED)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    item_service = ItemService(db)
    return item_service.create_item(item=item, owner_id=current_user.id)

@router.get("/", response_model=List[ItemSchema])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    item_service = ItemService(db)
    items = item_service.get_items_by_owner(owner_id=current_user.id, skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=ItemSchema)
def read_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    item_service = ItemService(db)
    db_item = item_service.get_item(item_id=item_id)
    if db_item is None or db_item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=ItemSchema)
def update_item(
    item_id: int,
    item: ItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    item_service = ItemService(db)
    db_item = item_service.get_item(item_id=item_id)
    if db_item is None or db_item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_service.update_item(item_id=item_id, item_update=item)

@router.delete("/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    item_service = ItemService(db)
    db_item = item_service.get_item(item_id=item_id)
    if db_item is None or db_item.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item_service.delete_item(item_id=item_id)
    return {"message": "Item deleted successfully"}
