import matplotlib.pyplot as plt
import numpy as np

def gradient_image(ax, extent, direction=0.3, cmap_range=(0, 1), **kwargs):
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array(
        [[v @ [1, 0], v @ [1, 1]],
        [v @ [0, 0], v @ [0, 1]]]
    )
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(
        X,
        extent=extent,
        interpolation='bicubic',
        vmin=0, vmax=1, 
    **kwargs)

    return im
