import numpy as np
import matplotlib.pyplot as plt


def mandelbrotSet(per=0.001, t=2000):
    p=0
    plt.plot([1, -2], [1, -1], 'ro', markersize=0)
    plt.axes().set_aspect('equal')
    x=0
    y=0
    for real in np.arange(-2, 0.42, per):
        p+=per
        print(p/0.025)
        plt.plot(x, y, 'ro', color='black', markersize=1)
        for imag in np.arange(-1, 1, per):
            c = complex(real, imag)
            show_t = t
            an = complex(0)
            while True:
                if show_t == 0:
                    x=an.real
                    y=an.imag
                    break
                else:
                    show_t -= 1
                    an = an ** 2 + c
                    if (abs(an.real) >= 2 or abs(an.imag) >= 2):
                        break
                    else: continue
    plt.show()
if __name__ == "__main__":
    mandelbrotSet()
