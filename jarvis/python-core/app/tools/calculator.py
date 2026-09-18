import ast, operator

OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.Pow:operator.pow,ast.Mod:operator.mod}

def calculate(expression: str):
    def ev(node):
        if isinstance(node, ast.Expression): return ev(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value,(int,float)): return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in OPS: return OPS[type(node.op)](ev(node.left),ev(node.right))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op,(ast.UAdd,ast.USub)): return +ev(node.operand) if isinstance(node.op,ast.UAdd) else -ev(node.operand)
        raise ValueError("Unsupported expression")
    return ev(ast.parse(expression, mode="eval"))

def register_calculator(registry):
    from app.tools.registry import Tool
    registry.register(Tool("calculator", "Safely evaluate arithmetic expressions", calculate))
