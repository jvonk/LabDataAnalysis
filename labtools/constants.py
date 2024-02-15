import scipy.constants

# Natural unit definitions
hbar = 1
c = 1
mu_0 = 1
k_B = k = 1
m_e = 1

# From scipy
pi = scipy.constants.pi
alpha = scipy.constants.alpha

# Derived
epsilon_0 = 1 / (mu_0 * c**2)
e = (4 * pi * epsilon_0 * hbar * c * alpha) ** 0.5

if __name__ == "__main__":
    import doctest

    doctest.testmod()
