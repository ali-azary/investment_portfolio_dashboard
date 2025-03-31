import pandas as pd
import numpy as np

def compute_cumulative_returns(returns, weights):
    """Computes cumulative returns."""
    return (1 + returns.dot(weights)).cumprod()

def calculate_kpi_metrics(returns, optimal_weights):
    """Calculates key performance indicators."""
    years = (returns.index[-1] - returns.index[0]).days / 365
    cum_unconstrained = compute_cumulative_returns(returns, optimal_weights)
    CAGR = ((cum_unconstrained.iloc[-1]) ** (1/years) - 1) * 100
    annual_vol = returns.dot(optimal_weights).std() * np.sqrt(252) * 100
    annual_returns = returns.mean() * 252
    sharpe = annual_returns.dot(optimal_weights) / (annual_vol / 100)
    neg_vol = returns.dot(optimal_weights).clip(upper=0).std() * np.sqrt(252)
    sortino = annual_returns.dot(optimal_weights) / (neg_vol / 100)
    return CAGR, annual_vol, sharpe, sortino