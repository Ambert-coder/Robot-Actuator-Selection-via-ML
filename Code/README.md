# Reproducibility Materials

This folder provides a no-API entry point for checking the released product data, joint requirement data, and reported experiment summaries.

## Environment

Create an isolated Python environment and install the packages listed in `requirements.txt`.

```bash
python -m pip install -r requirements.txt
python reproduce_summary.py
```

## Scope

The released results include grouped validation, probability calibration, scoring-sensitivity, full-catalogue comparison, and fair LLM comparison summaries.

The LLM experiment is supplied as aggregate, non-sensitive metrics only. Raw prompts, generated reports, reviewer-blinding keys, and provider credentials are intentionally excluded. The supplied script does not invoke any external model or API.

## Re-running the model

The manuscript specifies the feature definitions, validation protocol, evidence schema, and scoring procedure. Reimplementation should use product-family grouped folds and must not place repeated LLM generations from the same task condition into independent statistical groups.
