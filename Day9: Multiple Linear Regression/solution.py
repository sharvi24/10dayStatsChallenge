# Enter your code here. Read input from STDIN. Print output to STDOUT
# Sample input
# 2 7
# 0.18 0.89 109.85
# 1.0 0.26 155.72
# 0.92 0.11 137.66
# 0.07 0.37 76.17
# 0.85 0.16 139.75
# 0.99 0.41 162.6
# 0.87 0.47 151.77
# 4
# 0.49 0.18
# 0.57 0.83
# 0.56 0.64
# 0.76 0.18

import numpy
m,n=map(int,input().split())
entries=[None]*n
for i in range(n):
    entries[i]=list(map(float, input().split()))
    
n2=int(input())
entries2= [None]*n2 
for i in range(n2):
    entries2[i]=list(map(float, input().split())) 

input_matrix = numpy.asarray(entries)
input_matrix2 = numpy.asarray(entries2)

Y=input_matrix[:,[m]] 
X=input_matrix[:,:-1]
X2=input_matrix2[:,:]

new_column = [[1]*n]
X = numpy.insert(X, 0, new_column, axis=1)
new_column2 = [[1]*n2]
X2 = numpy.insert(X2, 0, new_column2, axis=1)

Xt=numpy.transpose(X)
C=numpy.dot(numpy.dot(numpy.linalg.inv(numpy.dot(Xt,X)),Xt),Y)

result=numpy.dot(X2,C)
list1 = result.tolist()
for i in list1:print(i[0])
