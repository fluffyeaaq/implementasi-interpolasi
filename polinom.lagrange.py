import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_new):
    def L(k, x):
        term = [(x - x[j]) / (x[k] - x[j]) for j in range(len(x)) if j != k]
        return np.prod(term, axis=0)

    y_new = sum(y[k] * L(k, x_new) for k in range(len(x)))
    return y_new

# Data points
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])
x_new = np.linspace(5, 40, 100)
y_new_lagrange = lagrange_interpolation(x, y, x_new)

plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_new_lagrange, '-', label='Lagrange interpolation')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.title('Lagrange Interpolation')
plt.show()
