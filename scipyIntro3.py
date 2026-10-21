import scipy.integrate as integrate
import scipy.special as special
def integrand (x, a, b):
    return x**2
a = 1
b = 0
result = integrate.quad(integrand, 0, 1, args=(a, b))
print(result)