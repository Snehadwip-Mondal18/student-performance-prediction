"""Data loading and basic schema validation for the student-risk demo."""
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = [
    "student_id", "previous_gpa", "attendance_percentage", "quiz_average",
    "assignment_average", "midterm_score", "assignment_submission_rate",
    "lms_activity", "study_hours", "assessment_trend", "at_risk"
]
NUMERIC_FEATURES = [c for c in REQUIRED_COLUMNS if c not in {"student_id", "at_risk"}]

def load_dataset(path):
    df = pd.read_csv(path)
    missing = sorted(set(REQUIRED_COLUMNS) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df["student_id"].isna().any():
        raise ValueError("student_id contains missing values")
    if df["student_id"].duplicated().any():
        raise ValueError("student_id must be unique")
    if not set(df["at_risk"].dropna().unique()).issubset({0, 1}):
        raise ValueError("at_risk must contain binary labels 0/1")
    return df

if __name__ == "__main__":
    default_path = Path(__file__).resolve().parents[2] / "data" / "raw" / "synthetic_student_performance.csv"
    data = load_dataset(default_path)
    print(f"Loaded {len(data)} records and {len(data.columns)} columns")
    print("Synthetic data only: do not interpret as real-world evidence.")
