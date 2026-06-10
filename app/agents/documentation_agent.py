def documentation_agent(state):

    print("\nDocumentation Agent Running")

    state["documentation"] = f"""
# Project Documentation

Requirement:
{state['requirement']}

Backend:
{state['backend_code']}

Frontend:
{state['frontend_code']}

Database:
{state['database_schema']}
"""

    return state