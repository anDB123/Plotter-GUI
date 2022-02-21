import matplotlib.pyplot as plt
import numpy as np
def plot_xy_scatter(x_values,y_values,title,x_axis_label,y_axis_label):
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, 50, "0.0", lw=2)
    ax.scatter(x_values, y_values, 50, "1.0", lw=0)
    ax.scatter(x_values, y_values, 40, "C1", lw=0, alpha=0.1)

    ax.set_title(title)
    ax.set_xlabel(x_axis_label)
    ax.set_ylabel(y_axis_label)

    plt.show()