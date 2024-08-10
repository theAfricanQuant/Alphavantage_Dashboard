# Alphavantage Dashboard

This project is an **Alphavantage Dashboard** designed to provide an interactive interface for analyzing financial data using the Alphavantage API. The dashboard is built using Quarto and Python, and it integrates various tools and libraries to provide comprehensive data visualization and analysis.

## Features

- **Data Visualization**: The dashboard includes several charts and tables to visualize financial data.
- **Automated Build and Deployment**: GitHub Actions are used to automate the build and deployment of the dashboard to GitHub Pages.
- **Python Integration**: The dashboard uses Python for data processing, with dependencies managed via a `requirements.txt` file.
- **Custom Styling**: The dashboard includes custom styling through a `custom.scss` file.

## Project Structure

- **`.github/workflows/publish.yml`**: GitHub Actions workflow file for automating the build and deployment process.
- **`Alphavantage_Dashboard.qmd`**: The main Quarto markdown file for the dashboard.
- **`Alphavantage_Dashboard.html`**: The generated HTML file for the dashboard.
- **`Alphavantage_Dashboard_files/`**: Directory containing all supporting libraries and assets for the dashboard.
- **`config.py`**: Python configuration file for setting up API keys and other configurations.
- **`dashboard_utils.py`**: Utility functions used in the dashboard.
- **`requirements.txt`**: List of Python dependencies required for the project.
- **`custom.scss`**: Custom styles for the dashboard.

## Getting Started

### Prerequisites

- **Python 3.11+**: Ensure you have Python 3.11 or later installed.
- **Quarto**: Install Quarto for rendering the dashboard.
- **Git**: Version control system.

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Alphavantage_Dashboard.git
   cd Alphavantage_Dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:
   - Edit the `config.py` file to include your Alphavantage API key.

### Usage

1. **Run the dashboard locally**:
   ```bash
   quarto preview Alphavantage_Dashboard.qmd
   ```

2. **Deploy the dashboard**:
   - Push your changes to the `main` branch. The GitHub Actions workflow will automatically build and deploy the dashboard to GitHub Pages.

### Troubleshooting

- If the workflow fails, ensure that your `requirements.txt` and `pyproject.toml` (if applicable) are correctly set up.
- Address any warnings regarding deprecated Node.js versions in the GitHub Actions workflow.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


