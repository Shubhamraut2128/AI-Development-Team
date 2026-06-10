from app.graph.state import State

def backend_agent(state: State):
    print("\nBackend agent Running...")

    requirement = state.get("requirement", "No requirement provided")

    state["backend_code"] = f"""
Spring Boot Backend Generated

Requirement:
{requirement}

Generated Modules:
- Controller Layer
- Service Layer
- Repository Layer
"""

    return state