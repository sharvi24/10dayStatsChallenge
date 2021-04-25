a=1.09
b=1
p=a/(a+b)
q=b/(a+b)

def factorial(z):
    n=1
    for i in range(1,z+1):n=n*i
    return n 

def perm(x,y):
    return factorial(x)/(factorial(x-y)*factorial(y))    

prob=0    
for i in range(3,7):
    prob=prob+perm(6,i)*(p**i)*(q**(6-i))

print(round(prob,3)) 
