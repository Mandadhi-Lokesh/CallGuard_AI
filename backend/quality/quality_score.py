import numpy as np

def compute_quality_factor(y):
    energy = np.mean(np.abs(y))

    if energy < 0.01:
        return 0.4
    if energy < 0.05:
        return 0.6
    return 1.0
