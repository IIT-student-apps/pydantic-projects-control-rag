from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pathlib import Path
from pydantic import PostgresDsn
from dotenv import load_dotenv
import os
import chromadb
from chromadb import Client
import chromadb.utils.embedding_functions as embedding_functions
from typing import ClassVar

load_dotenv()


BASE_DIR = Path(__file__).parent

# huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
#     api_key=settings.keys.HUGGING_FACE_KEY,
#     model_name=settings.chroma_db.chroma_ef,
# )


class ChromaDB:
    chroma_vector_model: str = "all-MiniLM-L6-v2"
    chroma_collection_name: str = "assistant"
    chroma_ef_name: str = os.getenv("HUGGING_EF")
    chroma_client: Client = Client()
    chroma_ef = embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=os.getenv("HUGGING_FACE_KEY"),
        model_name=chroma_ef_name,
    )
    collection = chroma_client.get_or_create_collection(
        name=chroma_collection_name,
        embedding_function=chroma_ef,
    )


class Keys(BaseSettings):
    TRELLO_TOKEN: str = os.getenv("TRELLO_TOKEN")
    HUGGING_FACE_KEY: str = os.getenv("HUGGING_FACE_KEY")


class Settings(BaseSettings):
    chroma_db: ChromaDB = ChromaDB()
    keys: Keys = Keys()


settings = Settings()
