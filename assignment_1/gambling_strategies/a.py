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
