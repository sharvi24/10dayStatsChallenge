# from scipy.stats import norm

# prob1=norm(loc = 20 , scale = 2).cdf(19.5)

# cdf_upper_limit = norm(loc = 20 , scale = 2).cdf(22)
# cdf_lower_limit = norm(loc = 20 , scale = 2).cdf(20) 
# prob2 = cdf_upper_limit - cdf_lower_limit

# print(round(prob1,3))
# print(round(prob2,3))

import math
mean, std = 20, 2

def cdf(x):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))
