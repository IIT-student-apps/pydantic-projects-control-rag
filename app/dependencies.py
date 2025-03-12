from config import settings
from services.test_service import ChromaService
from db.test_repository import ChromaDBRepository


def get_collection():
    return settings.chroma_db.collection


def get_service():
    chroma_service = ChromaService(ChromaDBRepository)
    return chroma_service


# import uuid

# # убрать потом
# from pydantic_ai import Agent
# from pydantic_ai.models.openai import OpenAIModel
# from pydantic_ai.providers.openai import OpenAIProvider


# def recursive_character_text_splitter(
#     text: str, chunk_size: int = 100, chunk_overlap: int = 10
# ):
#     chunks = []
#     start = 0

#     while start < len(text):
#         end = start + chunk_size

#         # Если конец превышает длину текста, добавляем оставшуюся часть
#         if end >= len(text):
#             chunks.append(text[start:])
#             break

#         # Добавляем текущий чанк
#         chunks.append(text[start:end])

#         # Обновляем start с учетом перекрытия
#         start += chunk_size - chunk_overlap

#     return chunks


# text = """
# Доска состоит из нескольких колонок: "Запланировано", "В процессе", "Готово" и "Архив".
# В команде работают три человека: Анна, разработчик; Игорь, тестировщик; и Светлана, менеджер проекта.
# В колонке "Запланировано" находятся задачи: "Реализовать функционал авторизации", за которую отвечает Анна с дедлайном 15 марта 2025 года;
# "Провести тестирование модуля авторизации", ответственным за которую является Игорь, дедлайн — 20 марта 2025 года;
# и "Подготовить документацию по авторизации", за которую отвечает Светлана, дедлайн — 18 марта 2025 года.
# В колонке "В процессе" находится задача "Разработка пользовательского интерфейса для авторизации", за которую отвечает Анна.
#  Дедлайн этой задачи — 10 марта 2025 года, и на данный момент она выполнена на 70%. В колонке "Готово" размещена задача "Создание базы данных для пользователей", также выполненная Анной с дедлайном 5 марта 2025 года.
#   В комментарии указано, что база данных успешно создана и протестирована. В архиве находится задача "Внедрение системы уведомлений",
#   завершенная Светланой с дедлайном 1 марта 2025 года, также с комментарием о успешном внедрении. Эта доска Trello позволяет команде
#   четко видеть, кто за что отвечает, какие задачи находятся в процессе выполнения, а какие завершены, что помогает менеджеру проекта
#   Светлане отслеживать прогресс и при необходимости перераспределять задачи."""

# cleaned_text = text.replace("\n", " ")


# def add_document(document: str, collection):

#     chunks = recursive_character_text_splitter(document)
#     ids = [str(uuid.uuid4()) for _ in range(len(chunks))]
#     collection.add(documents=chunks, ids=ids)
#     print(collection.count())
#     return chunks


# chr = get_collection()
# a = add_document(cleaned_text, chr)
# # for i in a:
# #     print("Chunks: ", i)

# chr.add(documents=["doc1"], ids="doc1")

# query = "Расскажи какие задачи есть в проекте и сколько людей работает в проекте"
# b = chr.query(query_texts=query, n_results=13)["documents"]
# # for c in b:
# #     for ic in c:
# #         print(ic)
# print(b)

# # ollama_model = OpenAIModel(
# #     model_name="llama3.2",
# #     provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
# # )

# # agent = Agent(
# #     ollama_model,
# # )
# # s_promt = f"ОТВЕЧАЙ ТОЛЬКО НА РУССКОМ.Я передам тебе сейчас контекст,а ты ответишь на запрос пользователя и отвечай только на русском.Контекст: {b}.Запрос пользователя: {query}"

# # result = agent.run_sync(s_promt)
# # print(result.data)
