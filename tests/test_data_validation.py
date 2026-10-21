from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data.load_data import load_dataset

def test_synthetic_dataset_schema():
    root = Path(__file__).resolve().parents[1]
    df = load_dataset(root / "data" / "raw" / "synthetic_student_performance.csv")
    assert len(df) > 0
    assert set(df["at_risk"].unique()).issubset({0, 1})
    assert df["student_id"].is_unique
