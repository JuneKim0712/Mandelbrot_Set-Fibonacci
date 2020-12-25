import numpy as np
import matplotlib.pyplot as plt


class msi:
    def __init__(self):
        self.clicked=False
        plt.title('stable')
        plt.plot([-1, 1], [0, 0], color='black')
        plt.plot([0, 0], [1, -1], color='black')
        plt.axes().set_aspect('equal')
        plt.connect('button_press_event', self.click)
        plt.connect('motion_notify_event', self.input)
        plt.show()
        return

    def ms(self, c):
        t = 1000
        z = np.array([0], dtype=complex)
        an = complex(0)
        while t > 0:
            t -= 1
            an = an ** 2 + c
            if (abs(an.real) >= 1 or abs(an.imag) >= 1):
                return [False, z]
            if an in z[:-1]:
                return [True, z]
            z = np.append(z, an)
        return [True, z]
 
    def click(self, event):
        if self.clicked == True:
            self.clicked = False
        elif event.dblclick==True:
            self.clicked = True
        return
 
    def input(self, event):
        if event.xdata == None or not self.clicked:
            return
        x = event.xdata
        y = event.ydata
        plt.cla()
        isStable, d = self.ms(complex(x, y))
        if isStable == True:
            color='black'
            plt.title('stable')
        else:
            color='red'
            plt.title('unstable')
        plt.plot([-1, 1], [0, 0], color='black')
        plt.plot([0, 0], [1, -1], color='black')
        plt.plot(d.real, d.imag, '-o', markersize=6, markerfacecolor='grey', color=color)
        plt.plot(x, y, 'ro', color='red', markersize=6)
        event.canvas.draw()
        return


if __name__ == "__main__":
    a=msi()