"""Train baseline and candidate models on the synthetic demonstration dataset."""
from pathlib import Path
import json
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (precision_score, recall_score, f1_score, roc_auc_score,
                             average_precision_score, accuracy_score, confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from src.data.load_data import load_dataset, NUMERIC_FEATURES
from src.features.preprocess import build_preprocessor

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "raw" / "synthetic_student_performance.csv"
OUT = ROOT / "reports" / "model_metrics.json"

def evaluate(name, model, X_train, X_test, y_train, y_test):
    pipe = Pipeline([("preprocess", build_preprocessor()), ("model", model)])
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    score = pipe.predict_proba(X_test)[:, 1] if hasattr(pipe.named_steps["model"], "predict_proba") else pred
    result = {
        "model": name,
        "accuracy": float(accuracy_score(y_test, pred)),
        "precision_at_risk": float(precision_score(y_test, pred, zero_division=0)),
        "recall_at_risk": float(recall_score(y_test, pred, zero_division=0)),
        "f1_at_risk": float(f1_score(y_test, pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_test, score)) if len(set(y_test)) > 1 else None,
        "pr_auc": float(average_precision_score(y_test, score)) if len(set(y_test)) > 1 else None,
        "confusion_matrix": confusion_matrix(y_test, pred).tolist()
    }
    return result

def main():
    df = load_dataset(DATA)
    X = df[NUMERIC_FEATURES]
    y = df["at_risk"].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    models = [
        ("majority_baseline", DummyClassifier(strategy="most_frequent")),
        ("logistic_regression", LogisticRegression(max_iter=2000, class_weight="balanced", random_state=42)),
        ("random_forest", RandomForestClassifier(n_estimators=250, min_samples_leaf=3, class_weight="balanced", random_state=42)),
        ("hist_gradient_boosting", HistGradientBoostingClassifier(max_iter=120, random_state=42))
    ]
    results = [evaluate(n, m, X_train, X_test, y_train, y_test) for n, m in models]
    OUT.write_text(json.dumps({
        "notice": "Illustrative metrics on synthetic data only; not valid evidence of real-world performance.",
        "random_state": 42, "test_size": 0.25, "results": results
    }, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    print(f"Saved illustrative metrics to {OUT}")
    print("WARNING: synthetic demonstration only; do not use for real student decisions.")

if __name__ == "__main__":
    main()
