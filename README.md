This repository contains a Python package for analyzing investment portfolios, including:

* **Data Acquisition:** Downloading asset price data from Yahoo Finance.
* **Portfolio Optimization:** Calculating optimal portfolio weights using Efficient Frontier and with constraints.
* **Performance Analysis:** Computing cumulative returns, CAGR, volatility, Sharpe ratio, Sortino ratio.
* **Risk Analysis:** Calculating Value at Risk (VaR) and Conditional Value at Risk (CVaR).
* **Attribution Analysis:** Performing Brinson attribution.
* **Monte Carlo Simulation:** Forecasting portfolio performance.
* **Stress Testing:** Evaluating portfolio performance under historical market stress scenarios.
* **Reporting:** Generating an HTML dashboard with key metrics and charts.

## Installation

1.  Clone the repository:

    ```bash
    git clone [repository URL]
    cd investment_portfolio
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate  # On Windows
    ```

3.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the `main.py` script:

    ```bash
    python main.py
    ```

2.  The generated HTML dashboard will be available at `reports/dashboard.html`. Open it in your web browser.

## Project Structure

```
investment_portfolio/
├── investment_portfolio/
│   ├── __init__.py
│   ├── data.py
│   ├── optimization.py
│   ├── performance.py
│   ├── risk.py
│   ├── attribution.py
│   ├── simulation.py
│   ├── plotting.py
│   ├── stress_test.py
│   ├── reporting.py
│   ├── utils.py
├── reports/
│   ├── assets/
├── dashboard_bootstrap.html
├── requirements.txt
├── README.md
├── main.py
├── .gitignore
```

## Modules

* **`data.py`:** Handles data downloading and cleaning.
* **`optimization.py`:** Performs portfolio optimization.
* **`performance.py`:** Calculates portfolio performance metrics.
* **`risk.py`:** Computes risk metrics (VaR, CVaR).
* **`attribution.py`:** Executes Brinson attribution.
* **`simulation.py`:** Runs Monte Carlo simulations.
* **`plotting.py`:** Generates various plots and charts.
* **`stress_test.py`:** Conducts stress test analysis.
* **`reporting.py`:** Creates the HTML dashboard.
* **`utils.py`:** Contains utility functions (if needed).
* **`main.py`:** Orchestrates the entire analysis.

## Configuration

* The `tickers`, `start_date`, and `end_date` variables in `main.py` can be modified to analyze different assets and time periods.
* The constraints in `optimization.py` can be adjusted to customize the constrained portfolio optimization.
* The Jinja2 template `dashboard_bootstrap.html` can be modified to change the appearance of the HTML report.

## Contributing

Feel free to contribute to this project by submitting pull requests.

