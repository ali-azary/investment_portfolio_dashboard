import pandas as pd

def compute_var_cvar(series, alpha):
    """Computes VaR and CVaR."""
    var = -series.quantile(1 - alpha)
    cvar = -series[series <= -var].mean()
    return var, cvar

def calculate_var_cvar_metrics(returns, optimal_weights, constrained_weights):
    """Calculates VaR and CVaR metrics."""
    var_metrics = []
    for label, series in [("Unconstrained", returns.dot(optimal_weights)), ("Constrained", returns.dot(constrained_weights))]:
        for alpha in [0.95, 0.99]:
            var, cvar = compute_var_cvar(series, alpha)
            var_metrics.append({"Portfolio": label, "Confidence": f"{int(alpha*100)}%", "VaR": round(var, 4), "CVaR": round(cvar, 4)})
    return pd.DataFrame(var_metrics)