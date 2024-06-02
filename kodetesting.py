import numpy as np

# Fungsi interpolasi Lagrange
def lagrange_interpolation(x, y, x_new):
    n = len(x)
    m = len(x_new)
    y_new = np.zeros(m)
    for i in range(m):
        for j in range(n):
            p = 1
            for k in range(n):
                if k != j:
                    p *= (x_new[i] - x[k]) / (x[j] - x[k])
            y_new[i] += y[j] * p
    return y_new

# Fungsi interpolasi Newton
def newton_interpolation(x, y, x_new):
    def divided_difference(x, y):
        n = len(x)
        coef = np.zeros(n)
        for i in range(n):
            coef[i] = y[i]
        for j in range(1, n):
            for i in range(n-1, j-1, -1):
                coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
        return coef
    
    coef = divided_difference(x, y)
    n = len(x)
    m = len(x_new)
    y_new = np.zeros(m)
    for i in range(m):
        p = coef[0]
        for j in range(1, n):
            term = coef[j]
            for k in range(j):
                term *= (x_new[i] - x[k])
            p += term
        y_new[i] = p
    return y_new

# Data untuk pengujian
x_test = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_test = np.array([40, 30, 25, 40, 18, 20, 22, 15])
x_new_test = np.linspace(5, 40, 100)

# Hasil yang diharapkan untuk metode interpolasi Lagrange
y_expected_lagrange = lagrange_interpolation(x_test, y_test, x_new_test)

# Hasil yang diharapkan untuk metode interpolasi Newton
y_expected_newton = newton_interpolation(x_test, y_test, x_new_test)

# Perbandingan hasil aktual dengan hasil yang diharapkan
tolerance = 1e-6
lagrange_pass = np.allclose(y_expected_lagrange, lagrange_interpolation(x_test, y_test, x_new_test), atol=tolerance)
newton_pass = np.allclose(y_expected_newton, newton_interpolation(x_test, y_test, x_new_test), atol=tolerance)

if lagrange_pass:
    print("Lagrange interpolation test passed!")
else:
    print("Lagrange interpolation test failed!")

if newton_pass:
    print("Newton interpolation test passed!")
else:
    print("Newton interpolation test failed!")