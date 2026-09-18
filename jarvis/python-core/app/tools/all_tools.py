from app.tools.calculator import register_calculator
from app.tools.clock import register_clock
from app.tools.system import register_system_tools
from app.tools.file_reader import register_file_tools

def register_all_tools(registry):
    register_calculator(registry)
    register_clock(registry)
    register_system_tools(registry)
    register_file_tools(registry)
