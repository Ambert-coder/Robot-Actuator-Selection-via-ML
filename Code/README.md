# Reproducibility Materials

This folder contains the released analysis notebooks and a no-API entry point for checking the product data, joint requirement data, and reported experiment summaries.

## Files

- `01_grouped_nested_validation.ipynb`: nested validation with manufacturer/product-family grouping to reduce information leakage.
- `02_probability_calibration.ipynb`: probability-calibration analysis and class-wise reliability diagnostics.
- `03_scoring_sensitivity.ipynb`: Monte Carlo sensitivity analysis for score weights and task-demand perturbations.
- `04_fair_llm_comparison.ipynb`: matched Ordinary-LLM versus EC-LLM comparison, automatic verification, and blinded-review preparation.
- `reproduce_summary.py`: no-API summary checker for the released data and aggregate results.
- `requirements.txt`: Python dependencies used by the released scripts and notebooks.

## Environment

Create an isolated Python environment and install the packages listed in `requirements.txt`.

```bash
python -m pip install -r Code/requirements.txt
python Code/reproduce_summary.py
```

Run these commands from the repository root. The notebooks retain the original experiment logic. Before re-running a notebook, set its `BASE_DIR` to the local repository or experiment-data directory.

## Scope

The released results include grouped validation, probability calibration, scoring-sensitivity, full-catalogue comparison, and fair LLM comparison summaries.

The LLM notebook includes the experiment and evaluation logic, but generated reports, completed reviewer materials, reviewer-blinding keys, and provider credentials are intentionally excluded. API calling is disabled by default; re-running that portion requires the user to supply their own compatible endpoint, model, credentials, and budget. The summary script never invokes an external model or API.

## Re-running the model

The manuscript specifies the feature definitions, validation protocol, evidence schema, and scoring procedure. Reimplementation should use product-family grouped folds and must not place repeated LLM generations from the same task condition into independent statistical groups.
