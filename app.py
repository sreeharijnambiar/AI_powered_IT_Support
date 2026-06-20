import streamlit as st

from retrieval import process_query
from create_ticket import create_ticket

st.set_page_config(
page_title="AI IT Support Assistant"
)

st.title("🛠️ AI IT Support Assistant")

# Session State

if "show_ticket_form" not in st.session_state:
    st.session_state.show_ticket_form = False

if "user_query" not in st.session_state:
    st.session_state.user_query = ""

query = st.chat_input("Describe your IT issue...")

if query:
    st.chat_message("user").write(query)

    result = process_query(query)

    if result["status"] == "FOUND":
        st.chat_message("assistant").write(result["response"])
        st.session_state.show_ticket_form = False
    else:
        st.session_state.show_ticket_form = True
        st.session_state.user_query = query

# Ticket Creation Form

if st.session_state.show_ticket_form:

    st.warning(
        "No related historical tickets found."
    )

    st.write(
    "Create a new support ticket."
    )

    with st.form("ticket_creation_form"):

        title = st.text_input(
            "Issue Title"
    )

        description = st.text_area(
        "Issue Description",
        value=st.session_state.user_query
    )

        priority = st.selectbox(
        "Priority",
        [
            "Low",
            "Medium",
            "High",
            "Critical"
        ]
    )

        root_cause = st.text_area(
        "Root Cause"
    )

        assigned_team = st.text_input(
        "Assigned Team"
    )

        submitted = st.form_submit_button(
        "Create Ticket"
    )

        if submitted:

            ticket_id = create_ticket(
            title,
            description,
            priority,
            root_cause,
            assigned_team
        )

            st.success(
            f"Ticket Created Successfully: {ticket_id}"
        )

            st.write(
            f"Ticket ID: {ticket_id}"
        )

            st.session_state.show_ticket_form = False
