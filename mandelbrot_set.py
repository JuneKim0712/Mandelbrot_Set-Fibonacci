import numpy as np
import matplotlib.pyplot as plt


def ms(c, t=500):
    an = complex(0)
    while t > 0:
        t -= 1
        an = an ** 2 + c
        
            return False
    return True

def mandelbrotSet(per=0.005, t=700):
    x = np.array([], dtype=float)
    y = np.array([], dtype=float)
    plt.plot([1, -2], [1, -1], 'ro', markersize=0)
    imag =1
    real = -2
    while imag > -1:
        while real < 0.5:
            c = complex(real, imag)
            t = 700
            an = complex(0)
            while t > 0:
                t -= 1
                an = an ** 2 + c
                if (abs(an.real) >= 2 or abs(an.imag) >= 2):
                    
            real += per
        real = -2
        imag -= per
        continue
    plt.plot(x, y, 'ro', color='black', markersize=0.75)

if __name__ == "__main__":
    mandelbrotSet(per=0.1, t=30000)