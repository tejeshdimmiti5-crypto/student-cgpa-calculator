from app.reasoning.actions import Action, ActionPlan

class DAGPlanner:
    """Dependency-aware planner for common JARVIS intents."""
    def build(self, goal: str) -> ActionPlan:
        text = goal.lower().strip()
        if not text:
            return ActionPlan(goal="", actions=[], confidence=1.0)

        if any(x in text for x in ("delete", "remove", "shutdown", "purchase", "send", "format")):
            return ActionPlan(
                goal,
                [Action("confirm", "delegate", "security", {"command": goal},
                        priority=100, requires_confirmation=True)],
                0.96,
                "Sensitive intent routed through explicit confirmation",
            )

        if any(x in text for x in ("research", "find information", "search")):
            return ActionPlan(goal, [
                Action("research", "agent", "research", {"query": goal}, priority=40),
                Action("verify", "agent", "validator", {"source_action":"research"}, ["research"], priority=30),
                Action("respond", "respond", "user", {"source_actions":["research","verify"]}, ["verify"], priority=10),
            ], 0.82, "Research → verification → response")

        if any(x in text for x in ("build", "create", "develop", "implement")):
            return ActionPlan(goal, [
                Action("analyze", "agent", "planner", {"goal":goal}, priority=20),
                Action("implement", "agent", "coder", {"goal":goal}, ["analyze"], priority=30),
                Action("test", "agent", "tester", {"goal":goal}, ["implement"], priority=40),
                Action("review", "agent", "validator", {"goal":goal}, ["test"], priority=25),
                Action("respond", "respond", "user", {"goal":goal}, ["review"], priority=10),
            ], 0.84, "Analyze → implement → test → review → response")

        if any(x in text for x in ("https://", "http://", "browse", "website", "web page", "visit ")):
            return ActionPlan(goal, [
                Action("browser", "agent", "browser", {"command":goal}, priority=30),
                Action("respond", "respond", "user", {}, ["browser"], priority=10),
            ], 0.88, "Browser → response")

        if any(x in text for x in ("run python", "execute python", "execute code")):
            return ActionPlan(goal, [
                Action("code", "agent", "code_execution", {"command":goal}, priority=30),
                Action("respond", "respond", "user", {}, ["code"], priority=10),
            ], 0.90, "Sandboxed execution → response")

        if any(x in text for x in ("image", "camera", "screenshot", "look at")):
            return ActionPlan(goal, [
                Action("vision", "agent", "vision", {"command":goal}, priority=30),
                Action("respond", "respond", "user", {}, ["vision"], priority=10),
            ], 0.80, "Vision input → response")

        return ActionPlan(goal, [
            Action("respond", "respond", "user", {"command":goal}, priority=10)
        ], 0.60, "Direct response");
