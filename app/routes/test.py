from fastapi import APIRouter, Depends
from schemas.schemas import UserQuery, TextResponse, TextContext
from dependencies import get_collection, get_service
from typing import Annotated, Any
from services.test_service import ChromaService


router = APIRouter(tags=["query"])


@router.post("/add_context")
def add_context(
    text: TextContext,
    chroma_service: Annotated[ChromaService, Depends(get_service)],
    collection: Annotated[Any, Depends(get_collection)],
) -> TextResponse:
    result = chroma_service.add_document(collection, text.text)
    return TextResponse(text=result)


@router.post("/query")
def query(
    text: TextContext,
    chroma_service: Annotated[ChromaService, Depends(get_service)],
    collection: Annotated[Any, Depends(get_collection)],
) -> TextResponse:
    result = chroma_service.query(text.text, collection)
    return TextResponse(text=result)
