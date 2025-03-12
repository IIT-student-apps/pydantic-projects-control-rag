from abc import ABC, abstractmethod
from typing import List
from fastapi import HTTPException
import uuid

# убрать потом
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


class AbstractRepository(ABC):

    @abstractmethod
    async def add_document():
        raise NotImplementedError


class ChromaDBRepository(AbstractRepository):

    def add_document(self, document: str, collection):

        clean_document = (
            document.replace("\n", " ").replace('"', '\\"').replace("\r", "")
        )

        chunks = self.recursive_character_text_splitter(clean_document)
        ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
        collection.add(documents=chunks, ids=ids)

        return clean_document

    def query(self, query: str, collection):

        ollama_model = OpenAIModel(
            model_name="llama3.2",
            provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
        )
        nearest_vectors = self.get_nearest_vector(query, collection)
        result_string = "".join(["".join(sub_array) for sub_array in nearest_vectors])
        agent = Agent(
            ollama_model,
        )
        s_promt = f"Я передам тебе сейчас контекст,а ты ответишь на запрос пользователя и отвечай только на русском.Контекст: {result_string}.Запрос пользователя: {query}"

        result = agent.run_sync(s_promt)
        return result.data

    def recursive_character_text_splitter(
        self, text: str, chunk_size: int = 100, chunk_overlap: int = 10
    ):
        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size

            if end >= len(text):
                chunks.append(text[start:])
                break

            chunks.append(text[start:end])

            start += chunk_size - chunk_overlap

        return chunks

    def get_nearest_vector(self, query_text, collection):

        nearest_vector = collection.query(
            query_texts=[query_text],
            n_results=10,
        )["documents"]
        return nearest_vector
