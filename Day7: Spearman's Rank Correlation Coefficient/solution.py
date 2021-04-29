# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))
rx ,ry=[None]*n,[None]*n
i=1

while max(x)>0:
    rx[x.index(max(x))]=i
    x[x.index(max(x))]=0
    ry[y.index(max(y))]=i
    y[y.index(max(y))]=0
    i=i+1
    
meanX=sum(rx)/n
meanY=sum(ry)/n
stdx = (sum([(i - meanX)**2 for i in rx]) / n)**0.5
stdy = (sum([(i - meanY)**2 for i in ry]) / n)**0.5

covariance = sum([(rx[i] - meanX) * (ry[i] -meanY) for i in range(n)])
coefficient=covariance/(n*stdx*stdy)

print(round(coefficient,3))  
