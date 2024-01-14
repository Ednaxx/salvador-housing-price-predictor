import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBRegressor
import joblib

from features.build_features import build_features

def create_pipeline(model, training_data):
    numerical_cols = training_data.select_dtypes(include='number').columns
    categorical_cols = training_data.select_dtypes(include='object').columns

    # Preprocessing for numerical data
    numerical_transformer = SimpleImputer(strategy='median')

    # Preprocessing for categorical data
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    #Bundling
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])

    return Pipeline(steps=[('preprocessor', preprocessor), ('model', model)])


def train_model(df):
    df = build_features(df)

    X = df.drop("prices", axis=1)
    y = df.prices

    model = XGBRegressor(
        random_state=1,
        n_jobs=6,
        learning_rate=0.1,
        n_estimators=200,
        max_depth=5
        )

    pipe = create_pipeline(model, X)
    pipe.fit(X, y)

    joblib.dump(pipe, "./models/xgb.pkl")

if __name__ == "__main__":
    df = pd.read_csv("./data/housing_data.csv", index_col="id")

    train_model(df)
