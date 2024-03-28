# Recommendation_algorithm/management/utils.py

import numpy as np
from sklearn.preprocessing import MinMaxScaler

def normalize_data(data):
    """
    Perform min-max normalization on the input data.

    Parameters:
        data (numpy.ndarray): Input data to be normalized.

    Returns:
        numpy.ndarray: Normalized data.
    """
    if not isinstance(data, np.ndarray):
        raise ValueError("Input data must be a NumPy array")

    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data.reshape(-1, 1))

    if np.any(np.isnan(normalized_data)) or np.any(np.isinf(normalized_data)):
        raise ValueError("Normalized data contains NaN or Inf values")

    return normalized_data
