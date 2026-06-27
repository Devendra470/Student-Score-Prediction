import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def train_model():

    # Load Dataset
    df = pd.read_csv("../data/raw/Student_Performance.csv")

    # Encode Categorical Feature
    df["Extracurricular Activities"] = df["Extracurricular Activities"].map({
        "Yes": 1,
        "No": 0
    })

    # Features and Target
    X = df.drop("Performance Index", axis=1)
    y = df["Performance Index"]

    # Split Dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save Model
    joblib.dump(model, "../models/linear_regression.pkl")

    print("✅ Model trained and saved successfully!")


if __name__ == "__main__":
    train_model()