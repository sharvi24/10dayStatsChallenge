import math
mean, std = 100*2.4, 10*2
#print(mean)

def cdf(x):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.4f}'.format(cdf(250)))
