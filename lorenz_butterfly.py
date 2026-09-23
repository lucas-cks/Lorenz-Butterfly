import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

# Constants
sigma = 10.0
r = 28.0
b = 8.0/3.0

def lorenz_euler(x0, y0, z0, F=0.0, dt=0.01, tmax=100):
    nsteps = int(tmax / dt) + 1
    t = np.linspace(0, tmax, nsteps)
    X = np.zeros(nsteps)
    Y = np.zeros(nsteps)
    Z = np.zeros(nsteps)
    X[0], Y[0], Z[0] = x0, y0, z0

    for i in range(nsteps-1):
        dX = sigma*(Y[i] - X[i]) + F
        dY = r*X[i] - Y[i] - X[i]*Z[i]
        dZ = X[i]*Y[i] - b*Z[i]
        X[i+1] = X[i] + dX * dt
        Y[i+1] = Y[i] + dY * dt
        Z[i+1] = Z[i] + dZ * dt

    return X, Y, Z, t


X, Y, Z, t = lorenz_euler(10.0, 0.0, 0.0)


# 3D Trajectory Plot 
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(X, Y, Z, lw=0.5, color='blue')
ax.set_title('Lorenz Attractor')
plt.savefig('lorenz_attractor.png')
plt.show()
