from matplotlib import pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg


class show_chart(FigureCanvasQTAgg):
    def __init__(self, index):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.index = index
        print("index: ", self.index)

        plt.close()
        plt.ion()
        self.loop()

    def loop(self):
        xpoints = np.array(["cat", "dog", "lion", "tiger"])
        ypoints = np.array([3, 8, 1, 10])

        self.ax.plot(xpoints, ypoints)