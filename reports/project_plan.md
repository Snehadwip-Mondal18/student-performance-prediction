# Week 1 Project Plan

## Project
Student Academic Performance Prediction & Early-Warning System

## Target
Binary academic-risk classification in the eventual technical implementation:
- 0 = Low Risk
- 1 = At Risk

## Candidate Inputs
- previous_gpa
- attendance_percentage
- quiz_average
- assignment_average
- midterm_score
- assignment_submission_rate
- lms_activity
- study_hours
- assessment_trend

## Prediction Cutoff
Only information available before the defined prediction date may be used as a model input. Final outcomes must not leak into the feature set.

## Pipeline
Problem Definition -> Data Collection -> Validation -> Cleaning -> EDA ->
Feature Engineering -> Model Training -> Validation -> Evaluation ->
Interpretation -> Reporting

## Model Selection Principle
Do not select a model only by raw accuracy. Consider recall, precision, F1,
PR-AUC, calibration, interpretability, stability, and practical intervention capacity.

## Deliverables
- Project planning report
- Three strategic diagrams
- 32-hour work plan
- GitHub-ready repository structure
