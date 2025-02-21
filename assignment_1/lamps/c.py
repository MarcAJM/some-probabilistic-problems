from main import get_expected_value, get_num_of_tests
from numpy import arange, linspace, zeros, mean

n = 100000 # Amount of experiments

# Get the sample mean by executing the experiments a few times and then calculating the mean.
def get_sample_mean(k, m, p):
    results = zeros(n)
    for l in range(n):
        for j in range(m):
            results[l] += get_num_of_tests(k, p)
    return mean(results)

for ki in arange(2, 5):
    for mi in arange(1, 5):
        for pi in linspace(0, 1, 21):
            sample_mean = get_sample_mean(ki, mi, pi)
            print(f"n={mi*ki:.0f}, k={ki:.0f}, p={pi:.2f}: "
                  f"sample_mean = {sample_mean:.4f} "
                  f"(with confidence interval [{sample_mean * 0.95:.4f},{sample_mean * 1.05:.4f}]), "
                  f"expected value = {mi * get_expected_value(ki, pi):.4f}")