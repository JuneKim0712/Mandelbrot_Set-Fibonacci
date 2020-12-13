import matplotlib.pyplot as plt
import numpy as np



def bn(n): return complex(((((1+5**0.5)/2) ** n) - (((1-5**0.5)/2) ** n))/5**0.5)

plt.plot('ro')
plt.show()