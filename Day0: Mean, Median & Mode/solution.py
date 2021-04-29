import numpy
from statistics import mode, StatisticsError
from collections import Counter

N = int(input())
X = list(map(int, input().split()))

print(numpy.mean(X))
print(numpy.median(X))
# check if multi-modal or not
try: 
    print(mode(X))
except StatisticsError:
    #(mode=wholeList)
    X.sort()
    #print(X[0])  
    # (mode=partList)
    print(Counter(X).most_common(1)[0][0])
