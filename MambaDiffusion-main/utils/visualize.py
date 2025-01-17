import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches


def visualize(figsize=(30, 30), path='./', cmap='viridis', **images):
    n = len(images)
    plt.figure(figsize=figsize)
    for i, (name, image) in enumerate(images.items()):
        plt.subplot(1, n, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.title(' '.join(name.split('_')).title().lower())
        plt.imshow(image, cmap=cmap)
    # plt.show()
    plt.tight_layout()
    plt.savefig(path)
    plt.close()