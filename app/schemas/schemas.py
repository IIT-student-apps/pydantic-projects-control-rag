from pydantic import BaseModel
from typing import List


class UserQuery(BaseModel):
    query: str
    context: str


class TextResponse(BaseModel):

    text: str


class TextContext(BaseModel):

    text: str


class VectorResponse(BaseModel):
    vectors: List[float]
