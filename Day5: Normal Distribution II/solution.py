
import math
mean, std = 70, 10

def cdf(x):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
perc1=cdf(60)*100
perc2=(1-cdf(60))*100
perc3=perc1

print(round(perc1,2))
print(round(perc2,2))
print(round(perc3,2))
