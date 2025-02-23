# Question b)
import numpy as np

def simulate_payout_probability(n_simulations=100000):
    count_8 = 0
    
    for _ in range(n_simulations):
        # Given we observed payouts (6,7), assume higher mean Poisson(6) is more likely
        if np.random.rand() < 0.9:  # Heuristic: More confidence in Poisson(6)
            payout = np.random.poisson(6)
        else:
            payout = np.random.poisson(3)
        
        if payout == 8:
            count_8 += 1
    
    return count_8 / n_simulations

prob_8 = simulate_payout_probability()
print(f"Estimated probability of next payout being 8: {prob_8:.3f}")
