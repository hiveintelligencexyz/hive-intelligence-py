import os
import pytest
from hive_intelligence.client import HiveSearchClient
from hive_intelligence.types import HiveSearchRequest, HiveSearchMessage


@pytest.mark.parametrize("search_input", [
    # Basic prompt
    HiveSearchRequest(prompt="What is current price of Eth?"),

    # # Prompt + temperature
    HiveSearchRequest(prompt="Token info of SAI", temperature=0.3),

    # # Prompt + top_k
    HiveSearchRequest(prompt="BTC token info", top_k=5),

    # Prompt + top_p
    HiveSearchRequest(prompt="top 5 crypto gainer coins", top_p=0.9),

    # Prompt + include_data_sources
    HiveSearchRequest(prompt="BTC price", include_data_sources=True),

    # Chat mode with messages
    HiveSearchRequest(messages=[
        HiveSearchMessage(role="user", content="What is current price of Eth?"),
        HiveSearchMessage(role="assistant", content="Who are you")
    ]),

    # # All fields together
    HiveSearchRequest(
        prompt="top 5 crypto loser coins",
        temperature=0.6,
        top_k=10,
        top_p=0.95,
        include_data_sources=False,
    ),
])
def test_hive_search_full_coverage(search_input):
    api_key = os.environ.get("HIVE_API_KEY")
    assert api_key, "Set HIVE_API_KEY as an environment variable"

    client = HiveSearchClient(api_key=api_key)
    response = client.search(search_input)

    assert isinstance(response.response, dict)
    assert hasattr(response, "isAdditionalDataRequired")
