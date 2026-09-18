from app.sandbox.code_executor import CodeSandbox

class ExecutionTools:
    def __init__(self):
        self.sandbox = CodeSandbox()

    def run_python(self, code: str) -> dict:
        return self.sandbox.run_python(code)

def register_execution_tools(registry):
    from app.tools.registry import Tool
    tools = ExecutionTools()
    registry.register(Tool("run_python", "Execute Python inside a bounded sandbox", tools.run_python, requires_confirmation=False))
