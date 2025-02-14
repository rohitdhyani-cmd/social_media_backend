from pydantic import BaseModel
from typing import Optional

from ..auth.schemas import UserBase


class Profile(UserBase):
    followers_count: Optional[int] = 0
    following_count: Optional[int] = 0

    class Config:
        from_attributes = True


class UserSchema(BaseModel):
    profile_pic: Optional[str] = None
    username: str
    name: Optional[str] = None

    class Config:
        from_attributes = True


class FollowingList(BaseModel):
    following: list[UserSchema] = []


class FollowersList(BaseModel):
    followers: list[UserSchema] = []