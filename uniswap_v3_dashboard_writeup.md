
# 🦄 Uniswap V3 Dashboard – Project Writeup

**Date:** May 21, 2025  
**Status:** In Progress  
**Built With:** Flask, HTML/CSS, Chart.js, Uniswap Subgraph

---

## ✅ Completed Features

### 🔍 Pool Cards
- Display top Uniswap V3 pools (Top 5 by Volume)
- Show:
  - Token pair (e.g., USDC/ETH)
  - Volume (USD)
  - TVL (USD)
  - Fee Tier (%)
  - Raw Liquidity Units
- Added links to:
  - Token0 and Token1 on Etherscan
  - Pool address on Etherscan
- Tooltip for Fee Tier explanation

### 💱 ETH → USDC Quote
- Uses Uniswap V3 Subgraph to fetch live ETH price
- User inputs ETH amount → sees USDC quote
- Quote formatted with fallback/error handling

### 📊 Charts
- **Line Chart** (7-day history):
  - TVL (USD)
  - Volume (USD)
- **Bar Chart**:
  - TVL across Top 5 Pools

### 🎨 UI/UX
- Sleek, modern Uniswap-inspired theme
- Cards with hover effects, border radius, shadows
- Color-coded metrics
- Full mobile-safe layout planned for later

---

## 📝 Planned Features

### 💱 Token Selectors *(Saved for Later)*
- Allow user to select:
  - `tokenIn` (e.g. DAI, ETH)
  - `tokenOut` (e.g. UNI, USDC)
- Enter amount and fetch quote
- Dynamic REST API fallback or subgraph logic

### 📈 Metrics + Filters
- Add:
  - 24h price change %
  - Volume/TVL percent changes
- Support:
  - Sorting by Volume, TVL
  - Filter pools by tokens

### 🧠 Enhancements
- Convert raw liquidity into estimated USD
- Display token logos via CoinGecko API
- Add sparkline charts for micro trends
- Add responsive layout

---

## 📌 Tech Stack

| Layer         | Tools                        |
|---------------|------------------------------|
| Frontend      | HTML5, CSS3, Chart.js        |
| Backend       | Python 3, Flask              |
| Data Sources  | Uniswap V3 Subgraph (The Graph) |
| APIs          | (Future) Uniswap REST API    |

---

## 🧪 Notes

- REST API had authentication issues; fallback to subgraph used
- Subgraph API key and pool ID managed via environment variables
- GraphQL query structure centralized in `queries.py`
- Routes built to be modular: `/`, `/api/subgraph-quote`, `/api/pool-history`, `/api/top-pools-tvl`

---

## 🚀 Next Milestone

> Add token selector UI and dynamic token-to-token quoting

---

