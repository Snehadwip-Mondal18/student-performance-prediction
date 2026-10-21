"""Leakage-aware preprocessing pipeline."""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.data.load_data import NUMERIC_FEATURES

def build_preprocessor():
    numeric = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
    return ColumnTransformer([("numeric", numeric, NUMERIC_FEATURES)], remainder="drop")
