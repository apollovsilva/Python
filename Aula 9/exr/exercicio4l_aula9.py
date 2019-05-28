import numpy as np

#métrica

eta = np.matrix('1 0 0 0; 0 -1 0 0; 0 0 -1 0; 0 0 0 -1')
print(eta)

#elemento
print(eta[3,3])

#transposta
print(np.transpose(eta))


#print(eta[
