from lamps_main import get_sample_mean, get_mean
from numpy import arange, linspace

for mi in arange(2, 21):
    for ki in arange(2, 21):
        for pi in linspace(0.2, 1, 5):
            sample_mean = mi * get_sample_mean(ki, pi)
            theoretical_mean = mi * get_mean(ki, pi)
            print(f"n={mi*ki:.0f}, k={ki:.0f}, p={pi:.1f}: sample_mean = {sample_mean:.4f} (with confidence interval [{sample_mean * 0.95:.4f},{sample_mean * 1.05:.4f}]), expected value = {theoretical_mean:.4f}")