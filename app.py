import requests
from flask import Flask, render_template, jsonify
from utils.fetch import fetch_graph_data
from graphql.queries import TOP_POOLS_QUERY, ETH_USDC_POOL_QUERY, POOL_DAILY_QUERY

app = Flask(__name__)

@app.route("/")
def index():
    pools_data = fetch_graph_data(TOP_POOLS_QUERY).get('pools', [])
    return render_template("index.html", pools=pools_data)

@app.route("/api/subgraph-quote")
def subgraph_quote():
    try:
        data = fetch_graph_data(ETH_USDC_POOL_QUERY)
        pools = data.get("pools", [])
        if not pools:
            print("❌ No pools returned in subgraph response.")
            return jsonify({"ethPriceUSD": 0})

        pool = pools[0]
        print("✅ Pool data:", pool)

        price = float(pool["token0Price"])  # 1 ETH = ? USDC
        return jsonify({"ethPriceUSD": price})
    except Exception as e:
        print(f"❌ Subgraph quote error: {e}")
        return jsonify({"ethPriceUSD": 0})

@app.route("/api/pool-history")
def pool_history():
    try:
        data = fetch_graph_data(POOL_DAILY_QUERY)
        daily = data.get("poolDayDatas", [])
        daily.reverse()  # Put in chronological order

        labels = [d["date"] for d in daily]
        tvl = [float(d["tvlUSD"]) for d in daily]
        volume = [float(d["volumeUSD"]) for d in daily]

        return jsonify({
            "labels": labels,
            "tvl": tvl,
            "volume": volume
        })
    except Exception as e:
        print("❌ Chart API error:", e)
        return jsonify({"labels": [], "tvl": [], "volume": []})
    
@app.route("/api/top-pools-tvl")
def top_pools_tvl():
    try:
        data = fetch_graph_data(TOP_POOLS_QUERY)
        pools = data.get("pools", [])
        labels = [f"{p['token0']['symbol']}/{p['token1']['symbol']}" for p in pools]
        tvls = [float(p["totalValueLockedUSD"]) for p in pools]
        return jsonify({"labels": labels, "tvls": tvls})
    except Exception as e:
        print("❌ Bar chart API error:", e)
        return jsonify({"labels": [], "tvls": []})


if __name__ == "__main__":
    app.run(debug=True)
