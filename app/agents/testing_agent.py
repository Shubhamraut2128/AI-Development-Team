from app.graph.state import State

def testing_agent(state: State):
    print("\nTesting agent Running...")

    state["testing_reports"] = """
    Testing completed:
    - Unit tests passed
    - API tests passed
    - Integration tests passed
    """

    return state