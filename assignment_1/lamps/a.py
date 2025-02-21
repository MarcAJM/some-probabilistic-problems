from numpy import linspace, zeros, mean
from main import get_expected_value, get_num_of_tests

n = 100000 # Amount of experiments

# Get the sample mean by executing the experiments a few times and then calculating the mean.
def get_sample_mean(k, p):
    results = zeros(n)
    for l in range(n):
        results[l] = get_num_of_tests(k, p)
    return mean(results)

# Do this a number of times with different k and different p to show that the theoretical mean is right.
for ki in linspace(2, 6, 5, dtype=int):
    for pi in linspace(0.05, 1, 20):
        sample_mean = get_sample_mean(ki, pi)
        expected_value = get_expected_value(ki, pi)
        print(f"k={ki:.0f}, p={pi:.2f}: "
              f"sample_mean = {sample_mean:.4f} "
              f"(with confidence interval [{sample_mean * 0.95:.4f}, {sample_mean * 1.05:.4f}]), "
              f"expected value = {expected_value:.4f}")