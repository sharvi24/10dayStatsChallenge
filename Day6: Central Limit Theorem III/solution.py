# import math
# mean, std = 100*500, 80*10

# print('{:.2f}'.format(mean-1.96*std))
# print('{:.2f}'.format(mean+1.96*std))

from math import sqrt

s = int(input()) #100
mean = int(input()) #500
std = int(input())  #80
interval = float(input())   #0.95
z = float(input())          #1.96
print(round(mean - (std / sqrt(s)) * z, 2))
print(round(mean + (std / sqrt(s)) * z, 2))c

# Task
# You have a sample of  values from a population with mean 500 and with standard deviation 80 . Compute the interval that covers the middle  of the distribution of the sample mean; in other words, compute  and  such that . Use the value of . Note that  is the z-score.
