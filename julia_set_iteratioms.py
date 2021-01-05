import numpy as np
import matplotlib.pyplot as plt
import time as ttt


class js:
    def __init__(self):
        per=0.01
        self.t=49
        self.colors=np.array([])
        for i in np.arange(1/2, 1, 1/12):
            for n in np.arange(1/2, 1, 1/8):
                for x in np.arange(1/2, 1, 1/4):
                    self.colors=np.append(self.colors, [i, n, x])
        self.colors=self.colors.reshape(48, 3)
        self.rlist=np.arange(-2, 2, per)
        self.ilist=np.arange(-1.25, 1.25, per)
        self.clicked=False
        plt.plot([-2], [2])
        plt.plot([2], [-2])
        plt.axes().set_aspect('equal')
        plt.connect('button_press_event', self.input)
        plt.axis('off')
        plt.show()
        return


    def input(self, event):
        if event.dblclick==False:
            return
        xi = event.xdata
        yi = event.ydata
        plt.cla()
        plt.plot([2, -2], [1.25, -1.25], 'ro', markersize=0)
        c = complex(xi, yi)
        for real in self.rlist:
            for imag in self.ilist:
                show_t = self.t
                an = complex(real, imag)
                while show_t > 0 and abs(an) <= 4:
                    show_t -= 1
                    an = an ** 2 + c
                    continue
                if show_t==0:
                    plt.plot(real, imag, 'ro', color=(0, 0, 0), markersize=2)
                elif show_t> 47:
                    pass
                else:
                    plt.plot(real, imag, 'ro', color=self.colors[show_t], markersize=2)
        plt.plot(xi, yi, 'ro', color=(1, 0, 0), markersize=3)
        plt.axis('off')
        event.canvas.draw()

if __name__ == "__main__":
    a=js()