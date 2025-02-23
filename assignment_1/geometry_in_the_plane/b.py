from main import sample
import matplotlib.pyplot as plt

num_of_samples = 10000000
x_samples, y_samples = sample(num_of_samples)

plt.hist(x_samples, bins = 100, density=True)
plt.xlabel('X values')
plt.ylabel('Density')
plt.title('Marginal Density of X')
plt.show()

plt.hist(y_samples, bins = 100, density=True)
plt.xlabel('Y values')
plt.ylabel('Density')
plt.title('Marginal Density of Y')
plt.show()

