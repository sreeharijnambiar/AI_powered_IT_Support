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
You are an Enterprise IT Support Analyst.

Analyze the user's issue and the retrieved historical tickets.

Tasks:

1. Compare the user issue with retrieved tickets.
2. Identify the most likely root cause.
3. Determine an appropriate priority.
4. Summarize the issue.
5. Provide exactly 3 resolution steps.
6. Mention the reference ticket IDs.

Use only the retrieved tickets.
Do not invent information.

Format:

Issue Summary:
...

Priority:
...

Likely Root Cause:
...

Resolution:
1.
2.
3.

Reference Tickets:

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

