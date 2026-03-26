from langgraph.graph import StateGraph, END
from agents.detector import detect
from agents.classifier import classify
from agents.fixer import fix_bug
from agents.critic import validate_fix


def should_retry(state):
    if not state.get("is_fixed") and state.get("retry_count", 0) < state.get(
        "max_retries", 2
    ):
        return "fixer"
    return "end"


def build_graph():
    graph = StateGraph(dict)

    graph.add_node("detector", detect)
    graph.add_node("classifier", classify)
    graph.add_node("fixer", fix_bug)
    graph.add_node("critic", validate_fix)

    graph.set_entry_point("detector")

    graph.add_edge("detector", "classifier")
    graph.add_edge("classifier", "fixer")
    graph.add_edge("fixer", "critic")

    graph.add_conditional_edges("critic", should_retry, {"fixer": "fixer", "end": END})

    return graph.compile()
