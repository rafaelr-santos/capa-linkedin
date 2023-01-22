import numpy as np

def rotationMatrix(theta):
    theta = np.radians(theta)
    return np.array(
        [[np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]]
    )