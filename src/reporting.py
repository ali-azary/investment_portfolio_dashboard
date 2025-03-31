from jinja2 import Environment, FileSystemLoader
import pandas as pd
import numpy as np

def generate_html_report(returns, optimal_weights, annual_returns, annual_cov, stress_df, var_df, brinson_df, final_vals):
    """Generates HTML report using Jinja2."""
    years = (returns.index[-1] - returns.index[0]).days / 365
    cum_unconstrained = (1 + returns.dot(optimal_weights)).cumprod()
    CAGR = ((cum_unconstrained.iloc[-1]) ** (1/years) - 1) * 100
    annual_vol = returns.dot(optimal_weights).std() * np.sqrt(252) * 100
    sharpe = annual_returns.dot(optimal_weights) / (annual_vol / 100)
    neg_vol = returns.dot(optimal_weights).clip(upper=0).std() * np.sqrt(252)
    sortino = annual_returns.dot(optimal_weights) / (neg_vol / 100)

    env = Environment(loader=FileSystemLoader("../templates/"))
    template = env.get_template("dashboard_bootstrap.html")

    context = {
        "date": returns.index[-1].strftime("%Y-%m-%d"),
        "CAGR": round(CAGR, 2),
        "Volatility": round(annual_vol, 2),
        "Sharpe": round(sharpe, 2),
        "Sortino": round(sortino, 2),
        "annual_returns": annual_returns.to_frame("Expected Return").to_html(classes="table"),
        "annual_cov": annual_cov.round(4).to_html(classes="table"),
        "weights": pd.Series(optimal_weights).to_frame("Weight").to_html(classes="table"),
        "stress_table": stress_df.to_html(classes="table"),
        "var_table": var_df.to_html(classes="table", index=False),
        "brinson_table": brinson_df.to_html(classes="table"),
        "mc_summary": pd.Series({
            "5th percentile": np.percentile(final_vals, 5),
            "Median": np.median(final_vals),
            "95th percentile": np.percentile(final_vals, 95)
        }).round(4).to_frame("Value").to_html(classes="table"),
        "var_plot": "assets/var_plot.png",
        "cvar_plot": "assets/cvar_plot.png",
        "brinson_plot": "assets/brinson_attribution.png",
        "mc_plot": "assets/monte_carlo_forecast.png",
        "cumulative_performance_plot" : "assets/cumulative_performance.png",
        "efficient_frontier_plot" : "assets/efficient_frontier.png",
        "correlation_heatmap" : "assets/corr_heatmap.html"
    }

    html = template.render(**context)
    with open("../reports/dashboard.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ Dashboard generated at reports/dashboard.html")