import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy.optimize import curve_fit
from scipy.special import erf
from scipy.stats import chi2

ds = pd.read_csv('DoubleMuRun2011A.csv')
print(ds.head())

invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1-ds.eta2)-np.cos(ds.phi1-ds.phi2) ))
print('The first five values calculated (in units GeV):')
print(invariant_mass[0:5])

# Let's limit the fit near to the peak of the histogram.
escolha = 0
expected = 0
while(escolha>4 or escolha<1):
    escolha = eval(input("Escolha 1, 2, 3 ou 4: Enter 1> Z, Enter 2> Upsilon, Enter 3> J/Psi ou Enter 4> Psi':  "))
    escolha = int(escolha)
    if escolha == 1:
        lowerlimit = 70
        upperlimit = 110
        expected = 91.1876
        #return 
    elif escolha == 2:
        lowerlimit = 9.15
        upperlimit = 9.75
        expected = 9.46030
        #return expected 
    elif escolha == 3:
        lowerlimit = 2.95
        upperlimit = 3.2
        expected = 3.096916
        #return expected
    else:
        lowerlimit = 3.55
        upperlimit = 3.78
        expected = 3.686111
        #return expected 

bins = eval(input('Insira a binagem desejada: '))

# Let's select the invariant mass values that are inside the limitations.
limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

#Let's create a histogram of the selected values.
histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))

# In y-axis the number of the events per each bin (can be got from the variable histogram).
# In x-axis the centers of the bins.
y = histogram[0]
x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )

# Let's define a function that describes Breit-Wigner distribution for the fit.
# E is the energy, gamma is the decay width, M the maximum of the distribution
# and a, b and A different parameters that are used for noticing the effect of
# the background events for the fit.
def expo(const, slope, x):
    """ An exponential curve. *NB* The constant is in the exponent! 
  params: const, slope """
    return np.exp(const + slope*x)

def line(intercept, slope, x):
    """ Just another name for pol1. """
    return slope*x + intercept

def breitwigner(E, gamma, M, a, b, A):
    ''' gamma (the full width at half maximum (FWHM) of the distribution)
        M (the maximum of the distribution)
        a (the slope that is used for noticing the effect of the background)
        b (the y intercept that is used for noticing the effect of the background)
        A (the "height" of the Breit-Wigner distribution) '''
    return a*E+b+A*( (2*np.sqrt(2)*M*gamma*np.sqrt(M**2*(M**2+gamma**2)))/(np.pi*np.sqrt(M**2+np.sqrt(M**2*(M**2+gamma**2)))) )/((E**2-M**2)**2+M**2*gamma**2)

def gaussian(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

#def crystalball(n, x, beta, m, loc, scale):
#    return crystallball.pdf(n, x, beta, m, loc, scale)

def crystalball(x, a, n, xb, sig):
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
while(choice>3 or choice<1):
    choice = eval(input("Escolha 1, 2 ou 3: Enter 1> Breit-Wigner, Enter 2> Gaussian ou Enter 3> Crystal-Ball: "))
    choice = int(choice)
    if choice == 1:
        print("gamma (the full width at half maximum (FWHM) of the distribution),\nM (the maximum of the distribution),\na (the slope that is used for noticing the effect of the background),\nb (the y intercept that is used for noticing the effect of the background),\nA (the height of the Breit-Wigner distribution)")
        initials_breit =  [float(x) for x in input('Preencha com os parâmetros da Briet-Wigner (gamma, M, a, b e A) dando apenas espaços entre eles: ').split()] #Para o Z:[4, 91, -2, 150, 13000] Para o Upsilon: [0.5 9.5 20 -80 200]
        # Let's import the module that is used in the optimization, run the optimization
        # and calculate the uncertainties of the optimized parameters.
        best_breit, covariance = curve_fit(breitwigner, x, y, p0=initials_breit, sigma=np.sqrt(y))
        error_breit = np.sqrt(np.diag(covariance))
        
        # Let's print the values and uncertainties that are got from the optimization.
        print("The values and the uncertainties from the optimization")
        print("")
        first = "The value of the decay width (gamma) = {} +- {}".format(best_breit[0], error_breit[0])
        second = "The value of the maximum of the distribution (M) = {} +- {}".format(best_breit[1], error_breit[1])
        third = "a = {} +- {}".format(best_breit[2], error_breit[2])
        fourth = "b = {} +- {}".format(best_breit[3], error_breit[3])
        fifth = "A = {} +- {}".format(best_breit[4], error_breit[4])
        chi2 = (((best_breit[1]-expected)**2)/best_breit[1]).sum()
        print(first)
        print(second)
        print(third)
        print(fourth)
        print(fifth)
        print("chi2: ", chi2)

        #while (chi2 > 0.05):
        #    initials_breit = [best_breit[0], best_breit[1],best_breit[2],best_breit[3],best_breit[4]]
        #    best_breit1, covariance1 = curve_fit(breitwigner, x, y, p0=initials_breit1, sigma=np.sqrt(y))
        #    error_breit1 = np.sqrt(np.diag(covariance1)
            
        plt.plot(x, breitwigner(x, *best_breit), 'r-', label='gamma = {}, M = {}'.format(best_breit[0], best_breit[1]))
        plt.xlabel('Invariant mass [GeV]')
        plt.ylabel('Number of event')
        plt.title('The Breit-Wigner fit')
        plt.legend()
        plt.show()


    elif choice == 2:
        initials_gauss =  [float(x) for x in input('Preencha com os parâmetros da Gauss (max(y), mean, sigma): ').split()] 
        # Let's import the module that is used in the optimization, run the optimization
        # and calculate the uncertainties of the optimized parameters.
        best_gauss, covariance = curve_fit(gaussian, x, y, p0=initials_gauss, sigma=np.sqrt(y))
        error_gauss = np.sqrt(np.diag(covariance))

        # Let's print the values and uncertainties that are got from the optimization.
        print("The values and the uncertainties from the optimization")
        print("")
        first = "The value of max(y) = {} +- {}".format(best_gauss[0], error_gauss[0])
        second = "The value of mean = {} +- {}".format(best_gauss[1], error_gauss[1])
        third = "The value of sigma = {} +- {}".format(best_gauss[2], error_gauss[2])
        chi2 = (((best_gauss[1]-expected)**2)/best_gauss[1]).sum()
        print(first)
        print(second)
        print(third)
        print("chi2: ", chi2)

        plt.plot(x, gaussian(x, *best_gauss), 'r-', label='mean = {}, sigma = {}'.format(best_gauss[1], best_gauss[2]))
        plt.xlabel('Invariant mass [GeV]')
        plt.ylabel('Number of event')
        plt.title('The Gaussian fit')
        plt.legend()
        plt.show()
        
    else:
        print("a (defines how the function decreases off peak), \n n (), \n mean (mean, orders the position of the center of the peak ), \n sigma (standard deviation, controls the width of the curve)")
        initials_crystal =  [float(x) for x in input('Preencha com os parâmetros da Crystal-Ball  (a, n, mean, sigma): ').split()] 
        # Let's import the module that is used in the optimization, run the optimization
        # and calculate the uncertainties of the optimized parameters.
        best_crystal, covariance = curve_fit(crystalball, x, y, p0=initials_crystal, sigma=np.sqrt(y))
        error_crystal = np.sqrt(np.diag(covariance))

        # Let's print the values and uncertainties that are got from the optimization.
        print("The values and the uncertainties from the optimization")
        print("")
        first = "The value of a = {} +- {}".format(best_crystal[0], error_crystal[0])
        second = "The value of n = {} +- {}".format(best_crystal[1], error_crystal[1])
        third = "The value of mean = {} +- {}".format(best_crystal[2], error_crystal[2])
        fourth = "The value of sigma = {} +- {}".format(best_crystal[3], error_crystal[3])
        chi2 = (((best_crystal[2]-expected)**2)/best_crystal[2]).sum()
        print(first)
        print(second)
        print(third)
        print(fourth)
        print("chi2: ", chi2)

        plt.plot(x, crystalball(x, *best_crystal), 'r-', label='x = {}, x0 = {}'.format(best_crystal[0], best_crystal[1]))
        plt.xlabel('Invariant mass [GeV]')
        plt.ylabel('Number of event')
        plt.title('The CrystalBall fit')
        plt.legend()
        plt.show()
