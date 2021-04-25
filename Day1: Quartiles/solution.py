#!/bin/python3

import math
import os
import random
import re
import sys
 
# Complete the 'quartiles' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as a parameter.

def median(array):
    n=len(array)
    if n%2!=0: return array[(n-1)//2]
    else: return int((array[(n-1)//2]+array[n//2])/2)
    
def quartiles(arr):
    n=len(arr)
    arr.sort()
    q1=median(arr[:(n//2)])
    q2=median(arr)
    q3=median(arr[(n+1)//2:])
    return [q1,q2,q3]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    data = list(map(int, input().split()))
    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
