import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from openai import OpenAI


model = SentenceTransformer("all-MiniLM-L6-v2")



# Connect to ChromaDB

client = chromadb.PersistentClient(path="./vectordb")
client.delete_collection("historical_tickets")
collection = client.get_or_create_collection(
name="historical_tickets"
)

# load CSV

df = pd.read_csv("data/historical_tickets.csv")
print("Rows:", len(df))
print(df.head())
for _, row in df.iterrows():
    print(row["ticket_id"])

documents = []
embeddings = []
metadatas = []
ids = []

for _, row in df.iterrows():

    document = f"""

    Ticket ID: {row['ticket_id']}

    Category: {row['category']}

    Priority: {row['priority']}

    Issue:
    {row['issue_description']}

    Root Cause:
    {row['root_cause']}

    Resolution:
    {row['resolution']}

    Assigned Team:
    {row['assigned_team']}

    """

    embedding = model.encode(document).tolist()

    documents.append(document)

    embeddings.append(embedding)

    ids.append(str(row["ticket_id"]))

    metadatas.append(
        {
            "ticket_id": str(row["ticket_id"]),
            "category": str(row["category"]),
            "priority": str(row["priority"]),
            "assigned_team": str(row["assigned_team"])
        }
    )

collection.add(
ids=ids,
documents=documents,
embeddings=embeddings,
metadatas=metadatas
)

print(f"{len(ids)} tickets successfully ingested into ChromaDB")
print(f"Collection Count: {collection.count()}")