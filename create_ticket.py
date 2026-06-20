import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
"all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
path="./vectordb"
)

collection = client.get_collection(
name="historical_tickets"
)

def create_ticket(
    title,
    description,
    priority,
    root_cause,
    assigned_team
    ):


    df = pd.read_csv(
        "data/historical_tickets.csv"
    )

    new_ticket_id = (
        "INC" +
        str(100000 + len(df) + 1)
    )

    new_row = {
        "ticket_id": new_ticket_id,
        "category": title,
        "priority": priority,
        "issue_description": description,
        "root_cause": root_cause,
        "resolution": "Pending Resolution",
        "assigned_team": assigned_team
    }
    

    df.loc[len(df)] = new_row

    df.to_csv(
        "data/historical_tickets.csv",
        index=False
    )

    document = f'''
    Ticket ID: {new_ticket_id}

    Category: User Reported

    Priority: {priority}

    Issue:
    {description}

    Root Cause:
    Pending Investigation

    Resolution:
    Pending Resolution

    Assigned Team:
    Service Desk
    '''

    embedding = model.encode(
        document
    ).tolist()

    collection.add(
        ids=[new_ticket_id],
        documents=[document],
        embeddings=[embedding],
        metadatas=[
            {
                "ticket_id": new_ticket_id,
                "category": title,
                "priority": priority,
                "issue_description": description,
                "root_cause": root_cause,
                "resolution": "Pending Resolution",
                "assigned_team": assigned_team
            }
        ]
    )
    print(new_ticket_id)

    return new_ticket_id