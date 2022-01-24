import math

import numpy as np
import random

#Random walk of prices are calculated under the assumption of log-returns
def normal_random_walk(start, steps, loc, shape):
    returns = np.zeros(steps)
    prices = np.zeros(steps)
    prices[0] = start
    for i in range(1,steps):
        returns[i] = random.normalvariate(mu=loc, sigma=shape) + returns[i-1]
        prices[i] = start*math.e**returns[i]
    return returns, prices

def t_random_walk(start, steps, loc, df, shape):
    returns = np.zeros(steps)
    prices = np.zeros(steps)
    prices[0] = start
    if df > 2:
        sigma = shape/math.sqrt(df/(df-2))
        for i in range(1,steps):
            returns[i] = loc + sigma*np.random.standard_t(size = 1, df=df) + returns[i-1]
            prices[i] = start*math.e**returns[i]
        return returns, prices
    else:
        print(' degrees of freedom < 2, second moment cannot be calculated ')

