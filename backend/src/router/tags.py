# import type hints
from typing import Dict, List
from sqlalchemy.orm import Session

# import dependencies
import os
from fastapi import APIRouter, Depends, HTTPException
from uuid import uuid4 # this is for creating image ids
from uuid import UUID
from database.database import get_session
from models.tags import Tag

# intialize new router
router = APIRouter()

# C = CREATE -> @router.post("")
# R = READ -> @router.get("/{id}")
# U = UPDATE -> @router.patch("/{id}")
# D = DELETE -> @router.delete("/{id}")
# L = LIST -> @router.get("")

@router.post("")
async def create_tag(tag: str, session: Session = Depends(get_session)) -> Tag:
    """[summary]

    Args:
        tag (str): [description]
        session (Session, optional): [description]. Defaults to Depends(get_session).

    Returns:
        Tag: [description]
    """

    # create a new image instance
    db_tags = Tag(tag = tag, tag_id = uuid4().hex)
    # register image in session
    session.add(db_tags)
    # save changes in database
    session.commit()
    # reload image from database
    session.refresh(db_tags)
    return db_tags

@router.get("")
def list_tags(session: Session = Depends(get_session)) -> List[Tag]:
    """[summary]

    Args:
        session (Session, optional): [description]. Defaults to Depends(get_session).

    Returns:
        List[Tag]: [description]
    """

    return session.query(Tag).all()
