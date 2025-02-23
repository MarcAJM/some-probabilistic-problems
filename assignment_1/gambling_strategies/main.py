# Question a)
import numpy as np

def simulate_profit(n_simulations=100000):
    play_cost = 5
    profits = []
    
    for _ in range(n_simulations):
        # Randomly assign Poisson(3) or Poisson(6) to Machine A with equal probability
        if np.random.rand() < 0.5:
            payout = np.random.poisson(3)
        else:
            payout = np.random.poisson(6)
        
        profit = payout - play_cost
        profits.append(profit)
    
    mean_profit = np.mean(profits)
    std_error = np.std(profits, ddof=1) / np.sqrt(len(profits))  # Standard error of the mean
    margin_of_error = 1.96 * std_error  # 95% confidence interval approximation using normal distribution
    confidence_interval = (mean_profit - margin_of_error, mean_profit + margin_of_error)
    
    return mean_profit, confidence_interval

expected_profit, conf_interval = simulate_profit()
print(f"Estimated expected profit: {expected_profit:.3f}")
print(f"95% Confidence Interval: ({conf_interval[0]:.3f}, {conf_interval[1]:.3f})")


# Question b)
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


# Question c)
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


# Question d)
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
