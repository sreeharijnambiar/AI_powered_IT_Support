import chromadb
from sentence_transformers import SentenceTransformer
from llm_response import generate_response

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="./vectordb"
)

collection = client.get_collection(
    name="historical_tickets"
)

def process_query(user_query):

    query_embedding = model.encode(user_query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    retrieved_tickets = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    for doc, metadata in zip(documents, metadatas):

        retrieved_tickets.append(
            {
                "ticket_id": metadata["ticket_id"],
                "category": metadata["category"],
                "priority": metadata["priority"],
                "assigned_team": metadata["assigned_team"],
                "content": doc
            }
        )

    response = generate_response(
        user_query,
        retrieved_tickets
    )

    return response