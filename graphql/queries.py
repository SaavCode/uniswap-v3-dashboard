TOP_POOLS_QUERY = """
{
  pools(first: 5, orderBy: volumeUSD, orderDirection: desc) {
    id
    feeTier
    liquidity
    token0 {
      id
      symbol
    }
    token1 {
      id
      symbol
    }
    volumeUSD
    totalValueLockedUSD
  }
}
"""

ETH_USDC_POOL_QUERY = """
{
  pools(
    where: {
      id: "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8"
    }
  ) {
    id
    token0 {
      symbol
    }
    token1 {
      symbol
    }
    token0Price
    token1Price
    feeTier
  }
}
"""

POOL_DAILY_QUERY = """
{
  poolDayDatas(first: 7, orderBy: date, orderDirection: desc, where: {
    pool: "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8"
  }) {
    date
    volumeUSD
    tvlUSD
  }
}
"""

