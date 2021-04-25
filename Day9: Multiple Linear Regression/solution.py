a=[95,85,80,70,60]
b=[85,95,70,65,70]

sum_a=sum(a)
mean_a=sum_a/5
sum_b=sum(b)
mean_b=sum_b/5

x_square=sum([i**2 for i in a])
xy=sum([a[i]*b[i] for i in range(5)])

b= (5*xy-(sum_a*sum_b))/(5*x_square - (sum_a)**2)
a=mean_b -b*mean_a
print(round(a + b*80,3))
