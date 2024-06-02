import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])
x_new = np.linspace(5, 40, 100)

# Newton Interpolation
def newton_interpolation(x, y, x_new):
    def divided_diff(x, y):
        n = len(y)
        coef = np.zeros([n, n])
        coef[:, 0] = y

        for j in range(1, n):
            for i in range(n - j):
                coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])

        return coef[0, :]

    def newton_poly(coef, x, x_new):
        n = len(coef) - 1
        p = coef[n]
        for k in range(1, n + 1):
            p = coef[n - k] + (x_new - x[n - k]) * p
        return p

    coef = divided_diff(x, y)
    y_new = newton_poly(coef, x, x_new)
    return y_new

# Interpolation results
y_new_newton = np.array([newton_interpolation(x, y, xi) for xi in x_new])

# Plotting the results
plt.figure(figsize=(8, 6))  # Adjusted figure size to fit only Newton interpolation plot

# Plot for Newton
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_new, y_new_newton, '-', label='Newton interpolation')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.title('Newton Interpolation')

plt.tight_layout()
plt.show()
