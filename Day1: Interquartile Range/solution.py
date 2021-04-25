#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'interQuartile' function below.
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs

def median(array):
    n=len(array)
    if n%2!=0: return array[(n-1)//2]
    else: return (array[(n-1)//2]+array[n//2])/2

def interQuartile(values, freqs):
    n=sum(freqs)
    newarr=[]
    for i in range(len(freqs)):
        for f in range(freqs[i]): newarr.append(values[i])
    newarr.sort()  
    print("{:.1f}".format(median(newarr[(n+1)//2:]) - median(newarr[:(n//2)])))      
        
    

if __name__ == '__main__':
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    interQuartile(val, freq)
