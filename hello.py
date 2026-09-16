from langchain.agents import create_agent
from langchain.tools import tool
from plyer import notification


@tool
def test_tool(x: str) -> str:
    """Show a desktop notification and return a result."""
    notification.notify(
        title="LangChain Notification",
        message=x,
        timeout=10,
    )
    return "Result"

tools = [test_tool]

agent_executor = create_agent(model=None, tools=tools)

if __name__ == "__main__":
    print(test_tool.invoke("This is a test notification."))
