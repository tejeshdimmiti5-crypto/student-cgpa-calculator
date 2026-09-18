from app.reasoning.actions import Action, ActionPlan

class DAGPlanner:
    """Turns common natural-language goals into dependency-aware executable actions."""

    def build(self, goal: str) -> ActionPlan:
        text = goal.lower().strip()
        if not text:
            return ActionPlan(goal="", actions=[], confidence=1.0)

        actions: list[Action] = []
        if any(x in text for x in ("research", "find information", "search")):
            actions = [
                Action("research", "agent", "research", {"query": goal}, priority=40),
                Action("verify", "agent", "validator", {"source_action": "research"}, ["research"], priority=30),
                Action("respond", "respond", "user", {"source_actions": ["research", "verify"]}, ["verify"], priority=20),
            ]
            return ActionPlan(goal, actions, 0.72, "Research → verification → response")

        if any(x in text for x in ("build", "create", "develop", "implement")):
            actions = [
                Action("analyze", "agent", "planner", {"goal": goal}, priority=20),
                Action("implement", "agent", "coder", {"goal": goal}, ["analyze"], priority=30),
                Action("test", "agent", "tester", {"goal": goal}, ["implement"], priority=40),
                Action("review", "agent", "validator", {"goal": goal}, ["test"], priority=25),
                Action("respond", "respond", "user", {"goal": goal}, ["review"], priority=10),
            ]
            return ActionPlan(goal, actions, 0.78, "Analyze → implement → test → review → response")

        if any(x in text for x in ("delete", "remove", "shutdown", "purchase", "send")):
            return ActionPlan(
                goal,
                [Action("confirm", "delegate", "security", {"command": goal}, priority=100, requires_confirmation=True)],
                0.65,
                "Sensitive action routed through security confirmation",
            )

        return ActionPlan(
            goal,
            [Action("respond", "respond", "user", {"command": goal}, priority=10)],
            0.55,
            "Single response action",
        )
