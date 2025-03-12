from ..schemas.schemas import UserQuery, VectorResponse
from sentence_transformers import SentenceTransformer

@app.post("/ask/")
async def ask_assistant(user_query: UserQuery):

    query_vector = convert_to_vector(user_query.query)
    context_vector = convert_to_vector(user_query.context)
    collection.add(documents=[user_query.context], embeddings=[context_vector])
    results = collection.query(query_vector, n_results=5)

    answer = generate_answer(results)

    return {"answer": answer}
