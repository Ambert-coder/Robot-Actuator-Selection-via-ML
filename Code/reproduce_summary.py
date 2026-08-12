"""Minimal no-API reproducibility checks for the submitted data and results package."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
RESULTS = ROOT / "Results"

products = pd.read_excel(DATA / "Actuator_Product_Dataset.xlsx", sheet_name="Actuator_Product_Dataset", skiprows=3)
tasks = pd.read_excel(DATA / "Joint_Task_Requirements.xlsx", sheet_name="Joint_Task_Requirements", skiprows=3)

print(f"Product samples: {len(products)}")
print("Architecture counts:")
print(products["Drive Type"].value_counts().sort_index())
print(f"Joint task conditions: {len(tasks)}")

grouped = pd.read_csv(RESULTS / "Experiment_Grouped_Validation" / "random_vs_grouped_summary.csv", header=[0, 1], index_col=0)
print("\nGrouped validation summary:")
print(grouped)

calibration = pd.read_csv(RESULTS / "Experiment_Probability_Calibration" / "calibration_summary.csv", header=[0, 1], index_col=0)
print("\nCalibration summary:")
print(calibration)

llm = pd.read_csv(RESULTS / "Experiment_Fair_LLM_Comparison" / "paired_comparison_statistics.csv")
print("\nMatched LLM comparison:")
print(llm[["metric", "ordinary_mean", "ec_llm_mean", "paired_sign_flip_pvalue"]])
