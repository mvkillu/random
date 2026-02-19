import random
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("random")


@mcp.tool()
def generate_random_number(limit: int) -> int:
    """Generates a random number from 0 to the upper limit"""
    return random.randint(0, limit)
