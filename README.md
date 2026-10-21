# Student Academic Performance Prediction & Early-Warning System

A Week 1–4 educational data-science project that demonstrates project planning, data validation, exploratory data analysis, leakage-aware preprocessing, baseline/model comparison, evaluation, and presentation planning.

> **Important limitation:** The included CSV is synthetic and generated for demonstration. It is not real student data and model scores are not evidence of performance in a real institution. Do not use this prototype to make decisions about real students.

## Completed deliverables

- **Week 1:** Project plan, strategy diagrams, objectives, data schema, success criteria and 32-hour work plan (original artifacts retained).
- **Week 2:** Synthetic demo dataset, schema validation, EDA figures, data-quality and cleaning report.
- **Week 3:** Preprocessing pipeline, leakage-aware split, baseline + Logistic Regression + Random Forest + Gradient Boosting, metrics output and evaluation notes.
- **Week 4:** Comprehensive report, presentation outline, visualization plan, recommendations, risks and responsible-use safeguards.

## Quick start

Use Python 3.10+ in a virtual environment.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python -m src.data.load_data
python -m src.models.train_model
python -m src.evaluation.evaluate
pytest -q
```

The training command writes `reports/model_metrics.json`. Review the synthetic-data warning in that file before using the numbers in a presentation.

## Repository structure

```text
student-performance-prediction-main/
├── data/raw/                 # Synthetic demo CSV + data notice
├── data/processed/           # Generated/processed outputs (not committed by default)
├── figures/                  # Week 1 diagrams and Week 2 EDA plots
├── notebooks/                # Space for optional notebooks
├── reports/                  # Week 1–4 reports and presentation outline
├── src/data/                 # Dataset loading and schema validation
├── src/features/             # Preprocessing pipeline
├── src/models/                # Training and comparison
├── src/evaluation/            # Metrics reader
├── tests/                     # Basic data validation test
└── requirements.txt
```

## Data dictionary

| Field | Meaning | Expected range / use |
|---|---|---|
| `student_id` | Synthetic record ID | Unique; excluded from model features |
| `previous_gpa` | Previous GPA | 0–10 |
| `attendance_percentage` | Attendance percentage | 0–100 |
| `quiz_average` | Average quiz score | 0–100 |
| `assignment_average` | Average assignment score | 0–100 |
| `midterm_score` | Midterm score | 0–100 |
| `assignment_submission_rate` | Assignment submission rate | 0–100 |
| `lms_activity` | Illustrative LMS activity index | Non-negative, synthetic scale |
| `study_hours` | Illustrative study hours | Non-negative |
| `assessment_trend` | Illustrative assessment trend score | 0–100 |
| `at_risk` | Synthetic binary target | 0 = not flagged, 1 = flagged |

## Methodology and safeguards

- Split data before fitting preprocessing; fit imputation/scaling only on training data through a pipeline.
- Exclude identifiers and all information that would not be available at the prediction cutoff.
- Compare models using precision, recall, F1, ROC-AUC, PR-AUC and confusion matrix—not accuracy alone.
- For real data, use appropriate authorization, data minimization, de-identification, access control, time-based validation, subgroup error checks and human review.
- Model associations are not causal explanations. The prototype must only be used for learning and demonstration.

## Week-by-week reports

See the four `.docx` reports in `reports/` and `reports/presentation_outline.md`.
