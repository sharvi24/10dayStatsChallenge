# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
lambda1=2.5
k=5

def factorial(z):
    n=1
    for i in range(1,z+1):n=n*i
    return n 

print(round((lambda1**k)* math.exp(-lambda1)/factorial(k),3))
