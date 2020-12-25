import numpy as np
import matplotlib.pyplot as plt


def js(per=0.01, t=100):
    x = np.array([], dtype=float)
    y = np.array([], dtype=float)
    plt.plot([1, -1], [1, -1], 'ro', markersize=0)
    imag =1
    real = -1
    while real < 1:
        while imag > -1:
            c = complex(0, 0)
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
                    if (abs(an.real) > 1 or abs(an.imag) > 1):
                        break
                    else: continue
            imag -= per
            continue
        imag = 1
        real += per
        continue
    plt.plot(x, y, 'ro', color='black', markersize=0.75)
    plt.show()
if '__main__' == __name__:
    js()