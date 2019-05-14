import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy.optimize import curve_fit
from scipy.special import erf
from scipy.stats import chi2

def crystalball(a, n, xb, sig, x):
    x = x+0j # Prevent warnings...
    #N, a, n, xb, sig = params
    if a < 0:
        a = -a
    if n < 0:
        n = -n
    aa = abs(a)
    A = (n/aa)**n * np.exp(- aa**2 / 2)
    B = n/aa - aa
    C = n/aa / (n-1.) * np.exp(-aa**2/2.)
    D = np.sqrt(pi/2.) * (1. + erf(aa/np.sqrt(2.)))
    N = 1. / (sig * (C+D))
    total = 0.*x
    total += ((x-xb)/sig  > -a) * N * np.exp(- (x-xb)**2/(2.*sig**2))
    total += ((x-xb)/sig <= -a) * N * A * (B - (x-xb)/sig)**(-n)
    try:
      return total.real
    except:
      return total
    return total

# Initial values for the optimization in the following order:
# gamma (the full width at half maximum (FWHM) of the distribution)
# M (the maximum of the distribution)
# a (the slope that is used for noticing the effect of the background)
# b (the y intercept that is used for noticing the effect of the background)
# A (the "height" of the Breit-Wigner distribution)

initials_breit = 0
initials_gauss = 0
initials_crystal = 0
choice = 0

print("a (defines how the function decreases off peak), \n n (), \n mean (mean, orders the position of the center of the peak ), \n sigma (standard deviation, controls the width of the curve), \n x()")
initials_crystal =  [1, 3, 0, 1]
x = np.linspace(-10, 4, 1000)
y = crystalball(*initials_crystal, x)

plt.plot(x,y)
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of event')
plt.title('The CrystalBall fit')
plt.legend()
plt.show()
