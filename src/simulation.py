import numpy as np
import matplotlib.pyplot as plt

def perform_monte_carlo_simulation(returns, optimal_weights, n_sims=5000, n_days=252):
    """Performs Monte Carlo simulation."""
    annual_returns = returns.mean() * 252
    annual_cov = returns.cov() * 252
    mean_daily = annual_returns / 252
    cov_daily = annual_cov / 252
    simulations = np.zeros((n_days, n_sims))

    for i in range(n_sims):
        path = np.random.multivariate_normal(mean_daily, cov_daily, size=n_days)
        simulations[:, i] = np.cumprod(1 + path.dot(optimal_weights))

    final_vals = simulations[-1, :]
    return final_vals

def plot_monte_carlo_simulation(final_vals):
    """Plots Monte Carlo simulation results."""
    fig, ax = plt.subplots()
    ax.hist(final_vals, bins=50)
    ax.set(title="Monte Carlo Forecast", xlabel="Portfolio Value", ylabel="Frequency")
    fig.savefig("../reports/assets/monte_carlo_forecast.png")
    plt.close(fig)