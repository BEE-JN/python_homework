import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#  numpy常用模块：
#

X1 = np.linspace(-100,100,100)
X2 = np.linspace(-100,100,100)
X1,X2 = np.meshgrid(X1,X2)
A = np.square(X1) + np.square(X2)
Z = 0.5 + ((np.sin(np.sqrt(A))) - 0.5) / (np.square(1.0 + 0.001*A))
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X1,X2,Z,rstride = 1, cstride = 1, cmap = 'rainbow')
plt.show()