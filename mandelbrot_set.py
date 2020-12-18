import numpy as np
import matplotlib.pyplot as plt


def mandelbrotSet(per=0.005, t=700):
    x = np.array([], dtype=float)
    y = np.array([], dtype=float)
    plt.plot([1, -2], [1, -1], 'ro', markersize=0)
    imag =1
    real = -2
    while imag > -1:
        while real < 0.5:
            c = complex(real, imag)
            show_t = t
            an = complex(0)
            while True:
                if show_t == 0:
                    x=np.append(x, real)
                    y=np.append(y, imag)
                    break
                else:
                    show_t -= 1
                    an = an ** 2 + c
                    if (abs(an.real) >= 2 or abs(an.imag) >= 2):
                        break
                    else: continue
            real += per
            continue
        real = -2
        imag -= per
        continue
    plt.plot(x, y, 'ro', color='black', markersize=0.75)

if __name__ == "__main__":
    mandelbrotSet(per=0.1, t=300000)