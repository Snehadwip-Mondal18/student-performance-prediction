"""Evaluation checklist and metrics-file reader."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[2]
METRICS = ROOT / "reports" / "model_metrics.json"
if __name__ == "__main__":
    if not METRICS.exists():
        print("Metrics not found. Run: python -m src.models.train_model")
    else:
        payload = json.loads(METRICS.read_text(encoding="utf-8"))
        print(payload.get("notice", ""))
        for row in payload.get("results", []):
            print(row["model"], "recall=", round(row["recall_at_risk"], 3), "F1=", round(row["f1_at_risk"], 3))
