#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'weightedMean' function below.
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W

def weightedMean(X, W):
    wsum=sum([X[i]*W[i] for i in range(len(X))])
    print(round(wsum/sum(W),1)) 

if __name__ == '__main__':
    n = int(input())
    vals = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    weightedMean(vals, weights)
