def database_agent(state):

    print("\nDatabase Agent Running")

    state["database_schema"] = """
CREATE TABLE employee(
    id BIGINT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
"""

    return state