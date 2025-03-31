import pandas as pd
import matplotlib.pyplot as plt

def stress_test_scenarios(returns, optimal_weights, constrained_weights):
    """Performs stress test analysis."""
    scenarios = {
        "2008 Financial Crisis": ("2007-10-01", "2009-03-31"),
        "COVID Crash": ("2020-02-15", "2020-04-30"),
        "Dot‑Com Bust": ("2000-03-01", "2002-10-01")
    }

    results = []
    for name, (start, end) in scenarios.items():
        period = returns.loc[start:end]
        if not period.empty:
            for label, weights in [("Unconstrained", optimal_weights), ("Constrained", constrained_weights)]:
                series = (1 + period.dot(weights)).cumprod()
                cum_ret = series.iloc[-1] - 1
                mdd = ((series - series.cummax()) / series.cummax()).min()
                results.append({"Scenario": name, "Portfolio": label, "Cumulative Return": round(cum_ret, 4), "Max Drawdown": round(mdd, 4)})

    stress_df = pd.DataFrame(results)
    stress_df.to_csv("../data/stress_test_results.csv", index=False)
    pivot = stress_df.pivot(index="Scenario", columns="Portfolio")

    for metric in ["Cumulative Return", "Max Drawdown"]:
        fig, ax = plt.subplots()
        pivot[metric].plot(kind="bar", ax=ax)
        ax.set_title(metric)
        fig.savefig(f"../reports/assets/{metric.lower().replace(' ', '_')}.png")
        plt.close(fig)

    return stress_df