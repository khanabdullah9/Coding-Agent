from langchain_core.messages import HumanMessage

from agent import agent

response = agent.invoke(
    dict(
        messages = [HumanMessage(content = "write python program to print factorial.")],
        project_name = ""
    )
)

for msg in response["messages"]:
    msg.pretty_print()