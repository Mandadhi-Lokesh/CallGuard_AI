from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import joblib
import tensorflow as tf

from build_dataset import build_dataset

X, y = build_dataset()

scaler = joblib.load("training/scaler.pkl")
model = tf.keras.models.load_model("training/model.h5")

X_scaled = scaler.transform(X)
preds = (model.predict(X_scaled) > 0.5).astype(int)

print(confusion_matrix(y, preds))
print(classification_report(y, preds, target_names=["HUMAN", "AI_GENERATED"]))
