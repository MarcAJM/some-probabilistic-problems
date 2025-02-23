# Question d)
import numpy as np

def simulate_prob_A_correct(n_simulations=100000):
    correct_count = 0
    
    for _ in range(n_simulations):
        # Randomly assign which machine has average payout 6
        if np.random.rand() < 0.5:
            true_A = 6
            true_B = 3
        else:
            true_A = 3
            true_B = 6
        
        # Simulate two rounds of play
        a1, a2 = np.random.poisson(true_A), np.random.poisson(true_A)
        b1, b2 = np.random.poisson(true_B), np.random.poisson(true_B)
        
        # Check if we identify A as the better machine
        if a1 > b1 and a2 > b2:
            if true_A == 6:
                correct_count += 1  # Correct identification
    
    return correct_count / n_simulations

prob_A_correct = simulate_prob_A_correct()
print(f"Estimated probability that A actually has mean 6 given our identification: {prob_A_correct:.3f}")
