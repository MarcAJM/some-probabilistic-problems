from main import get_sample_mean, get_expected_value
from numpy import arange, linspace

for ki in arange(2, 5):
    for pi in linspace(0, 1, 21):
        sample_mean = 0
        expected_value = 0
        for mi in arange(1, 5):
            sample_mean += get_sample_mean(ki, pi)
            expected_value += get_expected_value(ki, pi)
            print(f"n={mi*ki:.0f}, k={ki:.0f}, p={pi:.2f}: "
                  f"sample_mean = {sample_mean:.4f} "
                  f"(with confidence interval [{sample_mean * 0.95:.4f},{sample_mean * 1.05:.4f}]), "
                  f"expected value = {expected_value:.4f}")