import matplotlib.pyplot as plt
import numpy as np
import numpy.random as r
from treeFractal.branchBuilder import branchBuilder


def treeBuilder(ax, points, size, stop, color, rand_ampl = 20, i = 2):
    newpoints = []

    for s0 in points:
        angle = np.degrees((np.pi*30)/180)

        s2 = branchBuilder(s0, (s0[2]-angle+r.uniform(-rand_ampl,rand_ampl)), size)
        s3 = branchBuilder(s0, (s0[2]+angle+r.uniform(-rand_ampl,rand_ampl)), size)


        newpoints.append(s2)
        newpoints.append(s3)

        ax.plot([s0[0], s2[0]], [s0[1], s2[1]], color=color)
        ax.plot([s0[0], s3[0]], [s0[1], s3[1]], color=color)
    
    if i+1 == stop + 2 :
        return

    treeBuilder(ax, newpoints, size/1.3, stop, color, i=i+1)
    
    return
