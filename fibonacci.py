import matplotlib.pyplot as plt
import numpy as np


def comfib(per=0.01, limit=5, mode='nonlive'):
    if mode == 'nonlive':
        n = 0
        x, y = np.array([]), np.array([])
        while n < limit:
            re = complex(((((1+5**0.5)/2) ** n) - (((1-5**0.5)/2) ** n))/5**0.5)
            x = np.append(x, re.real)
            y = np.append(y, re.imag)
            n += per
        plt.ylabel('Imaginary number')
        plt.xlabel('Real number')
        plt.plot(x, y, markersize=0.1)
        plt.plot([0, re.real], [0, 0], color='#d1d1d1')
        plt.show()
        return
    else:
        n = 0
        x, y = np.array([]), np.array([])
        plt.ylabel('Imaginary number')
        plt.xlabel('Real number')
        while n < limit:
            re = complex(((((1+5**0.5)/2) ** n) - (((1-5**0.5)/2) ** n))/5**0.5)
            x = np.append(x, re.real)
            y = np.append(y, re.imag)
            plt.plot(x, y, markersize=1)
            plt.plot([0, re.real], [0, 0], color='#d1d1d1')
            plt.pause(0.000001)
            plt.cla()
            n += per
        

def ncomfib(per_n=0.01, limit=-5):
    n = 0
    per = per_n
    x, y = np.array([]), np.array([])
    while n > limit:
        re = complex(((((1+5**0.5)/2) ** n) - (((1-5**0.5)/2) ** n))/5**0.5)
        x = np.append(x, re.real)
        y = np.append(y, re.imag)
        n -= per

    plt.ylabel('Imaginary number')
    plt.xlabel('Real number')
    plt.plot(x, y)
    plt.plot([0, re.real], [0, 0], color='#d1d1d1')
    plt.show()
