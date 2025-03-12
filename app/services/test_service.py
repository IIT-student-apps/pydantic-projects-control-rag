from db.test_repository import AbstractRepository
from typing import Any


class ChromaService:

    def __init__(self, repo: AbstractRepository):
        self.repo = repo()

    def add_document(self, collection: Any, document: str):
        result = self.repo.add_document(document, collection)
        return result

    def query(self, query: str, collection: Any):

        result = self.repo.query(query, collection)
        return result
