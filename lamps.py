from numpy import random, zeros, mean, linspace, arange
from math import pow
import matplotlib.pyplot as plt

n = 100000 # Amount of experiments

# Execute the experiment one time and return the amount of tests it required.
def get_num_of_tests(k, p):
    bulb_statuses = random.rand(k) > p # Generate a random array of size k with boolean values whether they are broken or not.
    if sum(bulb_statuses) == len(bulb_statuses):
        return 1 # All lights work at once.
    else:
        return k + 1 # Turning the lights on in series didn't work.

# Get the sample mean by executing the experiments a few times and then calculating the mean.
def get_sample_mean(k, p):
    results = zeros(n)
    for l in range(n):
        results[l] = get_num_of_tests(k, p)
    return mean(results)

# Get the theoretical mean.
def get_mean(k, p):
    return k + 1 - k * pow(1-p, k)

# 1a: do this a number of times with different k and different p to show that the theoretical mean is right.
for ki in linspace(20, 100, 5, dtype=int):
    for pi in linspace(0.2, 1, 5):
        sample_mean = get_sample_mean(ki, pi)
        theoretical_mean = get_mean(ki, pi)
        print(f"k={ki:.0f}, p={pi:.1f}: sample_mean = {sample_mean:.4f} (with confidence interval [{sample_mean * 0.95:.4f}, {sample_mean * 1.05:.4f}]), expected value = {theoretical_mean:.4f}")

# 1b: identifying f(k)
k_values = arange(2, 51)
f_values = []
for ki in k_values:
    for pi in linspace(1, 0, 101):
        if get_mean(ki, pi) < ki:
            f_values.append(pi)
            break
plt.plot(k_values, f_values, linestyle='-')
plt.xlabel('k')
plt.ylabel('f(k)')
plt.show()

# 1c:
for mi in arange(2, 21):
    for ki in arange(2, 21):
        for pi in linspace(0.2, 1, 5):
            sample_mean = mi * get_sample_mean(ki, pi)
            theoretical_mean = mi * get_mean(ki, pi)
            print(f"n={mi*ki:.0f}, k={ki:.0f}, p={pi:.1f}: sample_mean = {sample_mean:.4f} (with confidence interval [{sample_mean * 0.95:.4f},{sample_mean * 1.05:.4f}]), expected value = {theoretical_mean:.4f}")