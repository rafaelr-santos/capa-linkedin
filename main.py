import matplotlib.pyplot as plt
import numpy.random as r

from background.gradient_image import gradient_image
from treeFractal.treeBuilder import treeBuilder
from treeFractal.branchBuilder import branchBuilder

xmin, xmax = xlim = 0, 1584
ymin, ymax = ylim = 0, 396

fig, ax = plt.subplots(1, 1, figsize=(39.6, 9.9))

ax.set(xlim=xlim, ylim=ylim, autoscale_on=False)

# background image
gradient_image(
    ax,
    direction=0,
    extent=(1, 0, 1, 0),
    transform=ax.transAxes,
    cmap=plt.cm.plasma,
    cmap_range=(0.2, 0.8),
    alpha=1
)

r.seed(3)
for i in range(10):
    size = r.uniform(50, 150)
    x = r.uniform(50, 1500)
    s1 = branchBuilder([x , 0], 90, size)
    ax.plot([x, s1[0]], [0, s1[1]], color="white")

    treeBuilder(
        ax = ax, size = size/2, stop = 9, color="white",
        rand_ampl = 20, points = [s1]
    )

ax.set_aspect('auto')
ax.axis("off")

plt.savefig("capa.png", bbox_inches="tight")
