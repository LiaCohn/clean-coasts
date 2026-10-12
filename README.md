# Clean Coast Index: Beach Cleanliness Assessment

An academic data science project exploring environmental, seasonal, and geographic factors associated with beach water-cleanliness measurements. The repository includes the project paper, source datasets, data-preparation notebooks, statistical analyses, visualizations, and machine-learning experiments.

## Project paper

The final project paper is included in the repository:

[`Clean Coast Index - A new approach for beach cleanliness assessment (1).pdf`](<Clean Coast Index - A new approach for beach  cleanliness assessment (1).pdf>)

## Project workflow

The notebooks cover the following stages:

1. **Prepare and enrich the data** - clean and combine cleanliness measurements with location, authority, weather, and geographic information; derive features such as season, recent rainfall, and distance to ports.
2. **Explore the data** - examine distributions, correlations, and patterns across locations and conditions.
3. **Test statistical differences** - use non-parametric Mann-Whitney U tests to compare cleanliness measurements across selected conditions and areas.
4. **Experiment with predictive models** - explore multiple linear regression, random-forest regression, and neural networks. The model notebooks include train/test splits and evaluation with regression metrics; the random-forest work also explores hyperparameter search.

The analyses are exploratory academic work. Results depend on the selected data, features, and notebook settings; this repository does not describe a deployed or production model.

## Repository structure

| Path | Contents |
| --- | --- |
| `Clean Coast Index - A new approach for beach  cleanliness assessment (1).pdf` | Final project paper |
| `clean_coast.xlsx`, `clean_coast_data.xlsx` | Cleanliness data and prepared analysis data |
| `authorities.xlsx`, `coordinates.xlsx` | Local authority and geographic reference data |
| `cleanup.ipynb`, `add_columns.ipynb` | Data cleanup, joins, and feature creation |
| `statistics/` | Correlation analysis, statistical tests, graphs, and results |
| `models/mlr/` | Multiple linear regression experiments |
| `models/random_forest/` | Random-forest experiments |
| `models/neural_networks/` | Neural-network experiments |
| `graphs/` | Exploratory visualizations |
| `models/utils.py` | Shared feature-cleanup helpers for model notebooks |

## Tools and methods

- Python, Jupyter Notebook, pandas, NumPy
- SciPy statistical tests and correlation analysis
- scikit-learn preprocessing, feature selection, regression, and evaluation
- Keras neural networks
- Excel datasets and geographic distance calculations with geopy

## Running the notebooks

The notebooks use relative paths to the spreadsheets and shared utilities. Clone the repository and run Jupyter from the repository root:

```bash
git clone https://github.com/LiaCohn/clean-coasts.git
cd clean-coasts
python -m venv .venv
source .venv/bin/activate
pip install jupyter pandas numpy openpyxl scipy scikit-learn matplotlib plotly geopy
jupyter notebook
```

For the neural-network notebooks, install a TensorFlow/Keras version compatible with your Python version and hardware. On Windows, activate the environment with `.venv\Scripts\activate`.

Run each notebook from its own directory so its relative data and utility paths resolve. Some notebooks are standalone analyses and use prepared spreadsheet files; inspect their first cells for the expected inputs before running.
