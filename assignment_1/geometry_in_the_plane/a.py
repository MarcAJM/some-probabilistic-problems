from numpy import arange, meshgrid, vectorize
import matplotlib.pyplot as plt
from main import sample

def jdf(x, y):
    if 0 < 2*y < x < 1:
        return 32.0*x*y
    else:
        return 0.0


num_of_samples = 100000000
x_samples, y_samples = sample(num_of_samples)

plt.hist2d(x_samples, y_samples, bins=100, cmap='Blues', density=True)
plt.colorbar(label='Density')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('2D Histogram')
plt.show()

x_range = arange(0, 1, 0.001)
y_range = arange(0, 0.5, 0.001)
X, Y = meshgrid(x_range, y_range) # Create a grid of x and y values.

# Vectorize the jdf function so it can accept arrays.
vectorized_jdf = vectorize(jdf)
Z = vectorized_jdf(X, Y)

plt.imshow(Z, extent=[x_range[0], x_range[-1], y_range[0], y_range[-1]],
           origin='lower', cmap='Blues', aspect='auto')
plt.colorbar(label='Density')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('2D Histogram using jdf(x, y)')
plt.show()


