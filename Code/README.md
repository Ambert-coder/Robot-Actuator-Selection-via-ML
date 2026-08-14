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

Clone the repository, create an isolated Python environment, and install the released dependencies:

```bash
git clone https://github.com/Ambert-coder/Robot-Actuator-Selection-via-ML.git
cd Robot-Actuator-Selection-via-ML
python -m pip install -r Code/requirements.txt
jupyter lab
```

Start Jupyter from the repository root, then open a notebook under `Code/`. When Jupyter starts from the repository root or `Code/`, the notebooks locate the repository automatically.

## Path configuration

The first code cell in every notebook supports explicit path overrides. Leave the variables unset for the standard cloned-repository layout. To use files in another location, either edit the corresponding override in the first code cell or set an environment variable before starting Jupyter.

### Repository root

The repository root must contain both `Code/` and `Data/`. It is detected by walking upward from the current working directory. To override it:

```python
REPO_ROOT_OVERRIDE = r"E:\path\to\Robot-Actuator-Selection-via-ML"  # Windows
# REPO_ROOT_OVERRIDE = "/home/user/Robot-Actuator-Selection-via-ML"  # macOS/Linux
```

Equivalent environment variables:

```bash
# Git Bash, macOS, or Linux
export ROBOT_ACTUATOR_REPO_ROOT="/path/to/Robot-Actuator-Selection-via-ML"
```

```powershell
# Windows PowerShell
$env:ROBOT_ACTUATOR_REPO_ROOT = "E:\path\to\Robot-Actuator-Selection-via-ML"
```

### Product dataset (`01` and `02`)

By default, both model-evaluation notebooks read:

```text
Data/Actuator_Product_Dataset.xlsx
```

The released worksheet is read as `Actuator_Product_Dataset` with `header=3`, which skips the title and description rows. To use another workbook, set:

```python
DATASET_PATH_OVERRIDE = r"E:\path\to\custom_dataset.xlsx"
```

or the `ROBOT_ACTUATOR_DATASET_PATH` environment variable. A custom workbook must preserve the released worksheet name, header position, target labels, and required feature columns unless the loading code is also adapted.

### Evidence packages (`03` and `04`)

These notebooks require one evidence-package JSON per task condition. The default directory is:

```text
Data/Evidence_Packages/
  03_xgboost_shap_physics_score_<condition-1>.json
  ...
  03_xgboost_shap_physics_score_<condition-8>.json
```

The evidence packages are not part of the current public release. Place a reviewed, non-sensitive package set in the default directory, or point to an external directory:

```python
EVIDENCE_DIR_OVERRIDE = r"D:\path\to\evidence_packages"
```

The equivalent environment variable is `ROBOT_ACTUATOR_EVIDENCE_DIR`. The notebooks only read JSON files directly inside the selected directory; they no longer scan unrelated directories or select a package set based on modification time.

### Output directories

New files are written below `Reproduced_Outputs/` and do not overwrite the released files under `Results/`.

- `01` and `02`: set `OUTPUT_DIR_OVERRIDE` or `ROBOT_ACTUATOR_OUTPUT_DIR` for a custom destination.
- `03`: set `OUTPUT_DIR_OVERRIDE` or `ROBOT_ACTUATOR_OUTPUT_DIR`.
- `04`: set `OUTPUT_DIR_OVERRIDE` or `ROBOT_ACTUATOR_LLM_OUTPUT_DIR`. Point this at an existing directory containing compatible `P*.json` files to resume or evaluate prior LLM generations.

The scoring-sensitivity notebook performs 10,000 Monte Carlo runs per task-condition/scenario pair by default and can take a substantial amount of time. For an installation smoke test only, set `ROBOT_ACTUATOR_MONTE_CARLO` to a small integer such as `20`. Restore or unset it for manuscript-scale reproduction; reported results use 10,000.

## LLM execution safety

`04_fair_llm_comparison.ipynb` keeps `RUN_LLM_CALLS = False` by default. In this mode it does not contact an external service or incur API charges. A full new generation run requires all of the following:

1. A complete evidence-package directory.
2. A compatible API endpoint and model configured in the first code cell.
3. `RUN_LLM_CALLS = True`.
4. A `DOGAPI_API_KEY` environment variable, or manual entry at the secure prompt.

Do not store credentials in the notebook, source files, generated JSON, or Git history. Model outputs can vary when the provider changes the hosted model, even when the sampling parameters and random seed are unchanged.

## Scope

The released results include grouped validation, probability calibration, scoring-sensitivity, full-catalogue comparison, and fair LLM comparison summaries.

The LLM notebook includes the experiment and evaluation logic, but generated reports, completed reviewer materials, reviewer-blinding keys, and provider credentials are intentionally excluded. API calling is disabled by default; re-running that portion requires the user to supply their own compatible endpoint, model, credentials, and budget. The summary script never invokes an external model or API.

## Re-running the model

Run the no-API repository check from the repository root with:

```bash
python Code/reproduce_summary.py
```

The manuscript specifies the feature definitions, validation protocol, evidence schema, and scoring procedure. Reimplementation should use product-family grouped folds and must not place repeated LLM generations from the same task condition into independent statistical groups.
