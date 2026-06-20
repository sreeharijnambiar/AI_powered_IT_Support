import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure Gemini

genai.configure(
api_key=os.getenv("API_KEY")
)

model = genai.GenerativeModel(
"gemini-2.5-flash"
)

SYSTEM_PROMPT = """
You are an IT Support Analyst.

Review the user issue and the retrieved historical tickets.

First determine if the retrieved tickets are actually related.

If related:

MATCH_FOUND

Then provide:

Issue Summary
Priority
Likely Root Cause
Resolution
Reference Tickets

If not related:

NO_MATCH

Only return NO_MATCH.
"""

def generate_response(user_query, retrieved_tickets):


    ticket_context = ""

    for ticket in retrieved_tickets:

        ticket_context += f"""


        Ticket ID: {ticket['ticket_id']}

        Category: {ticket['category']}

        Priority: {ticket['priority']}

        Assigned Team: {ticket['assigned_team']}

        Content:
        {ticket['content']}



        """


    prompt = f"""

    {SYSTEM_PROMPT}

    User Issue:
    {user_query}

    Retrieved Historical Tickets:
    {ticket_context}
    """


    response = model.generate_content(prompt)

    return response.text

