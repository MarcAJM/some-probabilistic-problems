from main import sample
import matplotlib.pyplot as plt

num_of_samples = 10000000
x_samples, y_samples = sample(num_of_samples)
z_samples = 2*(x_samples + y_samples)

plt.hist(z_samples, bins=100, density=True)
plt.xlabel("Z")
plt.ylabel("Density")
plt.show()