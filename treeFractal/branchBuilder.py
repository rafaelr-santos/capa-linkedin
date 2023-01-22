import numpy as np

def branchBuilder(s0, theta, size):
    thetaRad = np.radians(theta)

    s1 = [
        s0[0] + size*np.cos(thetaRad),
        s0[1] + size*np.sin(thetaRad),
        theta
    ]

    return s1