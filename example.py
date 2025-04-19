import os
from hive_intelligence.client import HiveSearchClient
from hive_intelligence.types import HiveSearchRequest, HiveSearchMessage

# Set your API key
api_key = os.environ.get("HIVE_API_KEY")
if not api_key:
    raise ValueError("Please set the HIVE_API_KEY environment variable")

# Initialize the client
client = HiveSearchClient(api_key=api_key)

# Example 1: Simple prompt-based query
prompt_request = HiveSearchRequest(
    prompt="What is the current price of Ethereum?"
)

response = client.search(prompt_request)
print("Prompt Response:")
print(response.model_dump())

# Example 2: Chat-based query using messages
chat_request = HiveSearchRequest(
    messages=[
        HiveSearchMessage(role="user", content="Price of"),
        HiveSearchMessage(role="assistant", content="Price of what?"),
        HiveSearchMessage(role="user", content="BTC")
    ]
)

response = client.search(chat_request)
print("\nChat Response:")
print(response.model_dump())
