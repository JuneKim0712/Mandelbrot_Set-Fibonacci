import numpy as np
import matplotlib.pyplot as plt


class msi:
    def __init__(self):
        theta = np.linspace(0, 2*np.pi, 100)
        r = np.sqrt(1.0)
        self.x1 = r*np.cos(theta)
        self.x2 = r*np.sin(theta)
        plt.plot(self.x1, self.x2, color='black')
        self.clicked=False
        plt.title('stable')
        plt.plot([-1.25, 1.25], [0, 0], color='black')
        plt.plot([0, 0], [1.25, -1.25], color='black')
        plt.axes().set_aspect('equal')
        plt.connect('button_press_event', self.click)
        plt.connect('motion_notify_event', self.input)
        plt.show()
        return
 
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
        plt.plot(self.x1, self.x2, color='black')
        plt.plot([-2, 2], [0, 0], color='black')
        plt.plot([0, 0], [2, -2], color='black')
        t=40
        d=np.array([complex(x, y)])
        plt.title('stable')
        while t > 0:
            t -= 1
            an=d[-1] ** 2
            if abs(d[-1]) > 1:
                d[:-1]
                plt.title('unstable')
                break
            else: d=np.append(d, an)
        plt.plot(d.real, d.imag, '-o', color='black', markersize=4)
        plt.plot(x, y, 'ro', color='red', markersize=6)
        event.canvas.draw()
        return


if __name__ == "__main__":
    a=msi()