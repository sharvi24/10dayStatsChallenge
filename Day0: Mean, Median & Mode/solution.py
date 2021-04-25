# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy
from statistics import mode, StatisticsError
from collections import Counter

N = int(input())
X = list(map(int, input().split()))

print(numpy.mean(X))
print(numpy.median(X))

# check if multi-modal or not [(mode=wholeList), (mode=partList)==> error thrown]
try: 
    print(mode(X))
except StatisticsError:
    X.sort()
    print(Counter(X).most_common(1)[0][0])
    
# Method-2 Mode
# def mode(arr):
#     cont = [X.count(i) for i in X];
#     return arr[cont.index(max(cont))];

