# Question c)
import numpy as np

def simulate_expected_T(n_simulations=100000):
    play_counts = []
    
    for _ in range(n_simulations):
        plays = 0
        identified = False
        
        while not identified:
            plays += 2  # Play both machines twice each round
            a1, a2 = np.random.poisson(3), np.random.poisson(3)
            b1, b2 = np.random.poisson(6), np.random.poisson(6)
            
            # Identify machine with the higher average payout
            if (a1 > b1 and a2 > b2) or (a1 < b1 and a2 < b2):
                identified = True
        
        play_counts.append(plays)
    
    mean_T = np.mean(play_counts)
    std_error = np.std(play_counts, ddof=1) / np.sqrt(len(play_counts))  # Standard error of the mean
    margin_of_error = 1.96 * std_error  # 95% confidence interval approximation using normal distribution
    confidence_interval = (mean_T - margin_of_error, mean_T + margin_of_error)
    
    return mean_T, confidence_interval

expected_T, conf_interval_T = simulate_expected_T()
print(f"Estimated E[T]: {expected_T:.4f}")
print(f"95% Confidence Interval for E[T]: ({conf_interval_T[0]:.4f}, {conf_interval_T[1]:.4f})")
