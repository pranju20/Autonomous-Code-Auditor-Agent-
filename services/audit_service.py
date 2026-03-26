from workflows.graph import build_graph
from input_output.input_handler import load_code_from_repo

graph = build_graph()


def run_audit(repo_path: str):
    code = load_code_from_repo(repo_path)
    result = graph.invoke({"code": code})
    return result
