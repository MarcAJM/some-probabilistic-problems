from numpy import arange, linspace
import matplotlib.pyplot as plt
from main import get_expected_value

k_values = arange(2, 51)
f_values = []
for ki in k_values:
    for pi in linspace(1, 0, 101):
        if get_expected_value(ki, pi) < ki:
            f_values.append(pi)
            break
plt.plot(k_values, f_values, linestyle='-')
plt.xlabel('k')
plt.ylabel('f(k)')
plt.show()