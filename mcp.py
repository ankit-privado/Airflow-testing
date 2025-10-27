from anyai import MCPClient
import json

def setup_mcp_connection():
    firstName = "name"
    mcp_server_url = "http://www.mcpServer.com"
    client = MCPClient("python -m mcp_server_filesystem /path/to/directory", mcp_server_url)
    tools = client.listTools(firstName)  # <<<==== This is our expected detection
    print(json.dumps(tools, indent=2))
    return tools
