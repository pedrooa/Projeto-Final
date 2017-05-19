import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

k = 2
x = 3
c = 2
m = 19

def EqDif(Y,t):
	x = Y[0]
	v = Y[1]
	dxdt = v
	dvdt = -(k*x/m) - (dxdt*v/m)
	return [dxdt, dvdt]


Y[0] = 0.01
Y[1] = 0
t = np.arange(0,5,0.01)
Sol = odeint(EqDif,(Y[0],Y[1]),t)

plt.plot(Sol[:,0], Sol[:,1])
plt.grid()
plt.show()