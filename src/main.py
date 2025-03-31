import data, optimization, performance, risk, attribution, simulation, plotting, stress_test, reporting
import pandas as pd
import numpy as np

tickers = ["SPY", "AGG", "VNQ", "GLD"]
start_date, end_date = "2010-01-01", "2024-03-27"
TRADING_DAYS = 252

prices, returns = data.download_and_clean_data(tickers, start_date, end_date)
annual_returns = returns.mean() * TRADING_DAYS
annual_cov = returns.cov() * TRADING_DAYS

optimal_weights, ef = optimization.optimize_portfolio(annual_returns, annual_cov)
constrained_weights = optimization.optimize_constrained_portfolio(annual_returns, annual_cov)

plotting.plot_efficient_frontier(annual_returns, annual_cov)

cum_unconstrained = performance.compute_cumulative_returns(returns, pd.Series(optimal_weights))
cum_constrained = performance.compute_cumulative_returns(returns, pd.Series(constrained_weights))
plotting.plot_cumulative_returns(cum_unconstrained, cum_constrained)

returns_extended = returns
scenarios = {
    "2008 Financial Crisis": ("2007-10-01", "2009-03-31"),
    "COVID Crash": ("2020-02-15", "2020-04-30"),
    "Dot‑Com Bust": ("2000-03-01", "2002-10-01")
}

for name, (start, end) in scenarios.items():
    if pd.to_datetime(start) < returns.index.min() or pd.to_datetime(end) > returns.index.max():
        prices = data.download_extra_data(tickers, start, end, prices)

returns_extended = prices.pct_change().dropna()

stress_df = stress_test.stress_test_scenarios(returns_extended, pd.Series(optimal_weights), pd.Series(constrained_weights))

plotting.plot_correlation_heatmap(returns)

var_df = risk.calculate_var_cvar_metrics(returns, pd.Series(optimal_weights), pd.Series(constrained_weights))
plotting.plot_var_cvar(var_df)

brinson_df = attribution.perform_brinson_attribution(returns, pd.Series(optimal_weights))
plotting.plot_brinson_attribution(brinson_df)

final_vals = simulation.perform_monte_carlo_simulation(returns, pd.Series(optimal_weights))
simulation.plot_monte_carlo_simulation(final_vals)

reporting.generate_html_report(returns, pd.Series(optimal_weights), annual_returns, annual_cov, stress_df, var_df, brinson_df, final_vals)