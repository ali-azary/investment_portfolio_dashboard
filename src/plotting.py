import matplotlib.pyplot as plt
import plotly.express as px
from pypfopt import plotting
import pandas as pd
from pypfopt import EfficientFrontier

def plot_correlation_heatmap(returns):
    """Plots correlation heatmap."""
    corr = returns.corr()
    px.imshow(corr, text_auto=True, title="Asset Correlation Matrix", labels=dict(x="Ticker", y="Ticker", color="Correlation")).write_html("../reports/assets/corr_heatmap.html", include_plotlyjs="cdn")

def plot_efficient_frontier(annual_returns, annual_cov):
    """Plots efficient frontier."""
    ef = EfficientFrontier(annual_returns, annual_cov)
    fig, ax = plt.subplots()
    plotting.plot_efficient_frontier(ef, ax=ax)
    ret, vol, _ = ef.portfolio_performance()
    ax.scatter(vol, ret, marker="*", s=200)
    ax.set(title="Efficient Frontier", xlabel="Volatility", ylabel="Return")
    fig.savefig("../reports/assets/efficient_frontier.png")
    plt.close(fig)

def plot_cumulative_returns(cum_unconstrained, cum_constrained):
    """Plots cumulative returns."""
    plt.figure()
    plt.plot(cum_unconstrained, label="Unconstrained")
    plt.plot(cum_constrained, label="Constrained")
    plt.title("Growth of $1 Invested")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.savefig("../reports/assets/cumulative_performance.png")
    plt.close()

def plot_brinson_attribution(brinson_df):
    """Plots Brinson attribution."""
    fig, ax = plt.subplots()
    brinson_df.plot(kind="bar", stacked=True, ax=ax)
    ax.set_title("Brinson Attribution")
    fig.savefig("../reports/assets/brinson_attribution.png")
    plt.close(fig)

def plot_var_cvar(var_df):
    # Plot bar chart
    fig, ax = plt.subplots()
    var_df.pivot(index="Confidence", columns="Portfolio", values="VaR").plot(kind="bar", ax=ax)
    ax.set_title("Value at Risk (VaR)")
    ax.set_ylabel("Daily Loss")
    fig.savefig("../reports/assets/var_plot.png")
    plt.close(fig)
    
    fig, ax = plt.subplots()
    var_df.pivot(index="Confidence", columns="Portfolio", values="CVaR").plot(kind="bar", ax=ax)
    ax.set_title("Conditional VaR (CVaR)")
    ax.set_ylabel("Daily Loss")
    fig.savefig("../reports/assets/cvar_plot.png")
    plt.close(fig)