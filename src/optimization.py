from pypfopt import EfficientFrontier
import pandas as pd

def optimize_portfolio(annual_returns, annual_cov):
    """Optimizes portfolio weights using Efficient Frontier."""
    ef = EfficientFrontier(annual_returns, annual_cov)
    ef.max_sharpe()
    optimal_weights = ef.clean_weights()
    pd.Series(optimal_weights).to_csv("../data/optimal_weights.csv", header=["Weight"])
    return optimal_weights, ef

def optimize_constrained_portfolio(annual_returns, annual_cov):
    """Optimizes portfolio with constraints."""
    ef_con = EfficientFrontier(annual_returns, annual_cov)
    ef_con.add_constraint(lambda w: w[ef_con.tickers.index("SPY")] >= 0.30)
    ef_con.add_constraint(lambda w: w[ef_con.tickers.index("AGG")] <= 0.60)
    ef_con.add_constraint(lambda w: w[ef_con.tickers.index("VNQ")] <= 0.20)
    ef_con.add_constraint(lambda w: w[ef_con.tickers.index("GLD")] <= 0.15)
    ef_con.max_sharpe()
    constrained_weights = ef_con.clean_weights()
    pd.Series(constrained_weights).to_csv("../data/constrained_weights.csv", header=["Weight"])
    return constrained_weights