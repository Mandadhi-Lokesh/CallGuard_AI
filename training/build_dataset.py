import os
import json
import numpy as np
from extract_features import extract_all_features

DATA_DIR = "training/data"
HUMAN_DIR = os.path.join(DATA_DIR, "human")
AI_DIR = os.path.join(DATA_DIR, "ai")

def build_dataset():
    X = []
    y = []

    for file in os.listdir(HUMAN_DIR):
        path = os.path.join(HUMAN_DIR, file)
        features = extract_all_features(path)
        X.append(features)
        y.append(0)  # HUMAN

    for file in os.listdir(AI_DIR):
        path = os.path.join(AI_DIR, file)
        features = extract_all_features(path)
        X.append(features)
        y.append(1)  # AI_GENERATED

    feature_order = [f"f_{i}" for i in range(len(X[0]))]

    with open("training/feature_order.json", "w") as f:
        json.dump(feature_order, f, indent=2)

    return np.array(X), np.array(y)
