from numpy import random, zeros, mean, linspace, arange
from math import pow

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
def get_expected_value(k, p):
    return k + 1 - k * pow(1-p, k)