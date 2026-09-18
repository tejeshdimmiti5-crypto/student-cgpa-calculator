from app.core.planner import Planner
from app.tasks.graph import TaskGraph

def test_planner():
    assert Planner().create_plan("hello") == ["hello"]

def test_task_graph():
    graph = TaskGraph()
    graph.add_task("A")
    graph.add_task("B", {"A"})
    assert graph.ready_tasks(set()) == ["A"]
    assert graph.ready_tasks({"A"}) == ["B"]
