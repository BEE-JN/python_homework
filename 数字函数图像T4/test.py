import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X1 = np.linspace(-10,10,100)
X2 = np.linspace(-10,10,100)
X1,X2 = np.meshgrid(X1,X2)
A = np.square(X1) + np.square(X2)
Z = pow(A,0.25) * (np.sin(50*pow(A,0.1)) + 1.0)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X1,X2,Z,rstride=1,cstride=1,cmap='rainbow')
plt.show()