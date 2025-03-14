from fastapi import FastAPI, HTTPException, APIRouter
import chromadb
from pydantic_ai import Agent

from fastapi.responses import ORJSONResponse
from config import settings
from fastapi.middleware.cors import CORSMiddleware
from routes.test import router as doc_rout
from start_app import start_app

origins = [
    # "http://localhost:8000",
    # "http://127.0.0.1:8000",
    #  front ports
]
app = start_app(create_custom_static_urls=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(doc_rout)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
