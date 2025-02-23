from numpy import random, sqrt

rng = random.default_rng()

def sample(n):
    u1 = rng.random(n)
    xs = u1 ** 0.25
    u2 = rng.random(n)
    ys = sqrt(u2) * xs / 2
    return xs, ys