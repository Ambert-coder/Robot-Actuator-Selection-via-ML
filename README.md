# Robot-Actuator-Selection-via-ML

The training datasets, machine learning code, and traceable large language model (LLM) explanations employed to facilitate the evidence-constrained selection of robotic joint actuator architectures.

This repository provides the supplementary materials for the AEI manuscript associated with the robotic actuator selection study. It is intended to support transparent review, archival access, and partial reproducibility of the reported data processing and analysis workflow.

## Repository Contents

- `Code/`: Reproducibility scripts for summarizing the released data and regenerating selected tables and figures from the supplementary materials.
- `Data/`: The curated actuator-product dataset, task-requirements dataset, and eight condition-specific evidence packages used in the case study.
- `Results/`: Selected validation, calibration, sensitivity, and LLM-comparison outputs that support the manuscript claims.
- `Supplementary_Materials_Description.md`: A concise human-readable overview of the supplementary files.

## Data Files

### 1. Actuator Product Dataset

`Data/Actuator_Product_Dataset.xlsx` contains 176 finalized actuator-product records and an English data dictionary. The file is designed to support inspection of the product-level evidence used in the manuscript's actuator selection workflow.

### 2. Joint Task Requirements

`Data/Joint_Task_Requirements.xlsx` contains eight static hip and knee task envelopes used in the case study. These task envelopes define the evidence-constrained operating context for the actuator-selection analysis.

### 3. Evidence Packages

`Data/Evidence_Packages/` contains eight condition-specific JSON evidence packages, one for each hip or knee task envelope. Each package records the joint requirements, all 176 candidate records, the ranked candidates, and the recommendation seed used by the scoring-sensitivity and fair LLM-comparison notebooks.

The released filenames and task-condition identifiers are in English. Source-dataset and task-requirement provenance fields use repository-relative paths so the files remain portable after cloning.

These packages contain structured engineering evidence rather than API credentials or raw provider responses. Their original feature labels are retained where necessary to preserve compatibility with the released source datasets and analysis workflow.

## Results Folder

The `Results/` directory contains selected aggregate outputs that summarize the main validation and sensitivity experiments:

- `Experiment_Grouped_Validation/`: grouped-vs-random validation comparisons, fold metrics, and group assignment audit tables.
- `Experiment_Probability_Calibration/`: calibration summaries, reliability diagnostics, and outer-fold calibration metrics.
- `Experiment_Scoring_Sensitivity/`: actuator-selection stability analyses under score perturbations.
- `Experiment_Fair_LLM_Comparison/`: paired comparison statistics and automatic metrics for the traceable LLM explanation comparison.

These files are included to document the behavior of the method under different evaluation settings and to make the reported figures and tables traceable.

## Code Folder

`Code/reproduce_summary.py` is a no-API Python script that inspects the released data and results package and reproduces selected summary outputs. The script is intended for local verification and does not require access to external model credentials.

The released analysis notebooks are organized in manuscript-workflow order:

- `Code/01_grouped_nested_validation.ipynb`: grouped nested-validation experiment.
- `Code/02_probability_calibration.ipynb`: probability-calibration experiment.
- `Code/03_scoring_sensitivity.ipynb`: scoring and task-demand sensitivity experiment.
- `Code/04_fair_llm_comparison.ipynb`: matched Ordinary-LLM versus EC-LLM comparison and evaluation workflow.

`Code/requirements.txt` lists the Python dependencies needed by the reproducibility script and notebooks. Historical cell outputs have been removed from the notebooks; all source-code cells are retained.

The notebooks resolve the cloned repository from the current working directory and write new files to `Reproduced_Outputs/`. The grouped-validation and calibration notebooks use the released product workbook directly. The scoring-sensitivity and LLM notebooks use the eight released JSON files under `Data/Evidence_Packages/`. See `Code/README.md` for Windows, macOS/Linux, Jupyter, path overrides, output-directory, and API configuration.

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/Ambert-coder/Robot-Actuator-Selection-via-ML.git
```

2. Install the Python dependencies:

```bash
pip install -r Code/requirements.txt
```

3. Run the reproducibility script from the repository root:

```bash
python Code/reproduce_summary.py
```

The script will read the released datasets and result files and print the main summary statistics to the console.

## Notes on Scope and Reproducibility

- This repository shares released supplementary materials only. It does not include private credentials, raw reviewer-blinding materials, or proprietary LLM access tokens.
- The eight per-condition evidence packages required by the scoring-sensitivity and LLM-generation workflows are included under `Data/Evidence_Packages/`; API calling remains disabled by default.
- The data files are curated artifacts for publication support and may not include the full internal working history of the study.
- If you reuse the materials, please cite the parent AEI manuscript and preserve the repository structure so that file paths remain stable.

## Citation

If this repository is useful for your work, please cite the corresponding AEI manuscript:

Zhang, A., Li, X.*, & Fu, Y. Evidence-Constrained Engineering Decision Support for Robot Joint Actuator Architecture Selection: Integrating Machine Learning, Physical Verification, and Traceable LLM Explanations. AEI manuscript.

## Corresponding Author

Xu Li  
State Key Laboratory of Robotics and Systems  
Harbin Institute of Technology  
Harbin 150001, China  
Email: hitlx@hit.edu.cn

## Author Information

- Aobo Zhang: aobo.zhang@stu.hit.edu.cn
- Xu Li: hitlx@hit.edu.cn
- Yili Fu: meylfu@hit.edu.cn

## Repository Use

This repository is prepared as the supplementary material package for the AEI manuscript and may be used for review, archival access, and controlled reproduction of the released analysis workflow.

## Contact

For questions about the released supplementary materials, please contact the corresponding author: Xu Li (`hitlx@hit.edu.cn`).
