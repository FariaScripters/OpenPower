from tools.sequential_thinking import SequentialThinkingTool
from tools.browser_tool import BrowserTool

def register_tools(server):
    """Register all available tools with the MCP server"""
    tools = [
        SequentialThinkingTool(),
        BrowserTool()
    ]
    
    for tool in tools:
        server.register_tool(tool.name, tool)
