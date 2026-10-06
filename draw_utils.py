import numpy as np
import matplotlib.pyplot as plt

def draw_plot(function_x, title:str):
    """Matplotlib draw helper function"""
    x = np.linspace(0, 100, 1000)
    figure, ax = plt.subplots()

    ax.plot(x, function_x(x))

    plt.title(title)