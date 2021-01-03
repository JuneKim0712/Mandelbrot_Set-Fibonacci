import numpy as np
import matplotlib.pyplot as plt


class js:
    def __init__(self):
        per=0.005
        self.rlist=np.arange(-2, 2, per)
        self.ilist=np.arange(-1.25, 1.25, per)
        self.clicked=False
        plt.plot([-2], [2])
        plt.plot([2], [-2])
        plt.axes().set_aspect('equal')
        plt.connect('button_press_event', self.click)
        plt.connect('motion_notify_event', self.input)
        plt.axis('off')
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
        xi = event.xdata
        yi = event.ydata
        plt.cla()
        t=50
        x = np.array([], dtype=float)
        y = np.array([], dtype=float)
        plt.plot([2, -2], [1.25, -1.25], 'ro', markersize=0)
        c = complex(xi, yi)
        for real in self.rlist:
            plt.plot(x, y, 'ro', color='black', markersize=3.75)
            plt.plot(xi, yi, 'ro', color='red', markersize=3)
            x = np.array([], dtype=float)
            y = np.array([], dtype=float)
            for imag in self.ilist:
                show_t = t
                an = complex(real, imag)
                while True:
                    if show_t == 0:
                        x=np.append(x, real)
                        y=np.append(y, imag)
                        break
                    else:
                        show_t -= 1
                        an = an ** 2 + c
                        if abs(an)>4:
                            break
                        else: continue
        
        plt.axis('off')
        event.canvas.draw()

if __name__ == "__main__":
    a=js()