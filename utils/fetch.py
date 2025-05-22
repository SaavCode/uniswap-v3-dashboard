import os
import requests
from dotenv import load_dotenv

# ✅ Load .env variables
load_dotenv()

# 🔐 Securely pulled from .env
GRAPH_API_KEY = os.getenv("GRAPH_API_KEY")
SUBGRAPH_ID = os.getenv("SUBGRAPH_ID")

# 🔗 Final endpoint
UNISWAP_GRAPH_URL = f"https://gateway.thegraph.com/api/{GRAPH_API_KEY}/subgraphs/id/{SUBGRAPH_ID}"

def fetch_graph_data(query):
    try:
        response = requests.post(UNISWAP_GRAPH_URL, json={"query": query})
        response.raise_for_status()
        result = response.json()

        if "data" in result:
            return result["data"]
        else:
            print("❌ GraphQL error:", result.get("errors"))
            return {}
    except Exception as e:
        print(f"❌ Exception during fetch: {e}")
        return {}
