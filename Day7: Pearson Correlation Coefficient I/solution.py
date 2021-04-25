n = int(input())
arrX = list(map(float,input().split()))
arrY = list(map(float,input().split()))

meanX=sum(arrX)/n
meanY=sum(arrY)/n
stdx = (sum([(i - meanX)**2 for i in arrX]) / n)**0.5
stdy = (sum([(i - meanY)**2 for i in arrY]) / n)**0.5

covariance = sum([(arrX[i] - meanX) * (arrY[i] -meanY) for i in range(n)])
coefficient=covariance/(n*stdx*stdy)

print(round(coefficient,3)) 
