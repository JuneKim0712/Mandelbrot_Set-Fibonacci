import numpy as np
import matplotlib.pyplot as plt


def ms(c):
    t = 50
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
 
def click(event):
    plt.connect('motion_notify_event', input)
    return
 
def input(event):
    if event.xdata == None:
        return
    x = event.xdata
    y = event.ydata
    plt.cla()
    isStable, d = ms(complex(x, y))
    if isStable == True:
        plt.title('stable')
    else:
        plt.title('unstable')
    plt.plot([-1, 1], [0, 0], color='black')
    plt.plot([0, 0], [1, -1], color='black')
    plt.plot(d.real, d.imag, '-o', markersize=6, markerfacecolor='gray', color='black')
    plt.plot(x, y, 'ro', color='red', markersize=6)
    event.canvas.draw()
 
def p(c):
    plt.title('stable')
    plt.plot([-1, 1], [0, 0], color='black')
    plt.plot([0, 0], [1, -1], color='black')
    d = ms(c)
    plt.plot(d[1].real, d[1].imag, '-o', markersize=6, markerfacecolor='gray', color='black')
    plt.plot(c.real, c.imag, 'ro', color='red', markersize=6)
    plt.connect('button_press_event', click)
    plt.show()

if __name__ == "__main__":
    p(0)