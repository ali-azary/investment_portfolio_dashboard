import pandas as pd

def perform_brinson_attribution(returns, optimal_weights):
    """Performs Brinson attribution analysis."""
    monthly_returns = returns.resample("M").apply(lambda x: (1 + x).prod() - 1)
    bench_weights = pd.Series(1/len(optimal_weights), index=optimal_weights.index)
    alloc = (pd.Series(optimal_weights) - bench_weights) * monthly_returns.sum()
    select = bench_weights * (monthly_returns.mean() - monthly_returns.mean().mean())
    brinson_df = pd.DataFrame({"Allocation Effect": alloc, "Selection Effect": select, "Total Effect": alloc + select}).round(4)
    return brinson_df