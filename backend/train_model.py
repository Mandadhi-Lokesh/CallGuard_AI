import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import os

def train_model():
    print("Training Model...")
    
    # CSV must contain extracted features + label column
    # label: 1 = AI, 0 = Human
    if not os.path.exists("training_data.csv"):
        print("Error: training_data.csv not found. Skipping training.")
        return

    df = pd.read_csv("training_data.csv")

    X = df.drop(columns=["label"])
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        random_state=42
    )

    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print("Validation accuracy:", acc)

    joblib.dump(model, "voice_auth_model.pkl")
    print("Model saved to voice_auth_model.pkl")

if __name__ == "__main__":
    train_model()
