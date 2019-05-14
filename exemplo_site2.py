import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#Generate some data:

np.random.seed(1234)
x = np.random.random(10)
y = 1.6*x + np.random.random(10)
#Perform the linear regression:

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("slope: %f    intercept: %f" % (slope, intercept))

#To get coefficient of determination (r_squared):

print("r-squared: %f" % r_value**2)

#Plot the data along with the fitted line:

plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()
plt.show()
