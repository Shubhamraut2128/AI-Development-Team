from langgraph.graph import StateGraph
from langgraph.graph import END

from app.graph.state import State

from app.agents.manager_agent import manager_agent
from app.agents.backend_agent import backend_agent
from app.agents.frontend_agent import frontend_agent
from app.agents.database_agent import database_agent
from app.agents.testing_agent import testing_agent
from app.agents.review_agent import review_agent
from app.agents.documentation_agent import documentation_agent

workflow = StateGraph(State)

workflow.add_node("manager", manager_agent)
workflow.add_node("backend", backend_agent)
workflow.add_node("frontend", frontend_agent)
workflow.add_node("database", database_agent)
workflow.add_node("testing", testing_agent)
workflow.add_node("review", review_agent)
workflow.add_node("documentation", documentation_agent)

workflow.set_entry_point("manager")

workflow.add_edge("manager", "backend")
workflow.add_edge("backend", "frontend")
workflow.add_edge("frontend", "database")
workflow.add_edge("database", "testing")
workflow.add_edge("testing", "review")
workflow.add_edge("review", "documentation")
workflow.add_edge("documentation", END)

graph = workflow.compile()