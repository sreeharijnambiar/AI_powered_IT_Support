# AI_powered_IT_Support
# AI Powered IT Support Assistant

## Overview

AI Powered IT Support Assistant is a Retrieval-Augmented Generation (RAG) based application that helps users troubleshoot IT issues using historical support tickets.

The system retrieves the most relevant tickets from a vector database, validates their relevance using an LLM, and generates a concise resolution summary. If no related ticket exists, the system allows users to create a new support ticket, which is automatically added to the knowledge base.

---

## Features

### Intelligent Ticket Search

* Converts user queries into embeddings.
* Performs semantic similarity search using ChromaDB.
* Retrieves the top 5 most relevant historical tickets.

### AI-Powered Analysis

* Uses Google Gemini to analyze retrieved tickets.
* Identifies:

  * Issue Summary
  * Priority
  * Likely Root Cause
  * Resolution Steps
* Returns concise and actionable support guidance.

### Ticket Validation

* Gemini validates whether retrieved tickets are relevant to the user's issue.
* If no relevant ticket exists, the system recommends creating a new support ticket.

### New Ticket Creation

* Collects:

  * Issue Title
  * Description
  * Priority
  * Root Cause
  * Assigned Team
* Generates a unique Incident ID.
* Stores the ticket in the historical ticket dataset.
* Automatically embeds and inserts the new ticket into ChromaDB.

### Ticket ID Lookup

* Supports direct ticket retrieval using Incident IDs.
* Example:

INC105001

Returns complete ticket details without performing semantic search.

---

## Architecture

User Query
↓
Embedding Model (all-MiniLM-L6-v2)
↓
ChromaDB Vector Search
↓
Top 5 Relevant Tickets
↓
Gemini Validation
↓
Match Found?
├── Yes → Generate Resolution
└── No → Create New Ticket
↓
Store in CSV
↓
Generate Embedding
↓
Insert into ChromaDB

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Vector Database

* ChromaDB

### Embedding Model

* Sentence Transformers
* all-MiniLM-L6-v2

### Large Language Model

* Google Gemini 2.5 Flash

### Data Storage

* CSV Dataset

---

## Project Structure

AI_powered_IT_Support/

├── app.py

├── retrieval.py

├── llm_response.py

├── create_ticket.py

├── inject.py

├── requirements.txt

├── data/

│   └── historical_tickets.csv

├── vectordb/

└── README.md

---

## Installation

Clone the repository:

git clone https://github.com/sreeharijnambiar/AI_powered_IT_Support.git

cd AI_powered_IT_Support

Create virtual environment:

python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

## Environment Variables

Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key

---

## Load Historical Tickets

Run:

python inject.py

This will:

* Read historical tickets.
* Generate embeddings.
* Store vectors in ChromaDB.

---

## Run Application

streamlit run app.py

---

## Example Queries

### Incident Resolution

Outlook email is not sending messages

VPN connection fails after password reset

Printer appears offline

### Ticket Lookup

INC105001

INC105050

---

## Future Enhancements

* Multi-turn conversation memory
* Ticket status tracking
* Automated ticket categorization
* Role-based access control
* Real-time ticket analytics dashboard
* Integration with ServiceNow/JIRA
* Agentic workflow orchestration

---

## Author

Sreehari J Nambiar

Python | AI Applications | Automotive Software Validation
