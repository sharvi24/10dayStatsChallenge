a=12
b=10
q=a/100
p=1-q

def factorial(z):
    n=1
    for i in range(1,z+1):n=n*i
    return n 

def perm(x,y):
    return factorial(x)/(factorial(x-y)*factorial(y))    

prob1=0    
for i in range(0,3):
    prob1=prob1+perm(10,i)*(q**i)*(p**(10-i))
prob2=0 
for i in range(2,11):
    prob2=prob2+perm(10,i)*(q**i)*(p**(10-i))    

print(round(prob1,3))    
print(round(prob2,3)) 
