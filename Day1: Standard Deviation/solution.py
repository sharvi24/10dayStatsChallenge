
import math
import os
import random
import re
import sys

# Complete the 'stdDev' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def squared_diff(arr,avg):
    sdiff=sum([(arr[i]-avg)**2 for i in range(len(arr))])
    return(sdiff)

def stdDev(arr):
    avg=sum(arr)/len(arr)
    stddev2= squared_diff(arr,avg)/len(arr)
    print(math.sqrt(stddev2))
    

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    stdDev(vals)
