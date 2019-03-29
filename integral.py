import math


def f(x):
    return(math.sin(x))

x1 = 0
x2 = math.pi

#aralik kaç parcaya bolunecek
n = 10
h = (x2-x1)/n
integral = 0

#kısakenar
for i in range(n):
	integral += f(x1+i*h)*h
print(integral)

#uzunkenar
integral = 0
for i in range(1,n+1):
	integral += f(x1+i*h)*h
print(integral)	

#ortanokta
integral = 0
for i in range(n):
    integral += f(x1+h/2+i*h)*h
print(integral)

#yamuk alanından yararlanarak
integral = 0
for i in range(n):
    integral += (f(x1+i*h)+f(x1+(i+1)*h))*h/2
print(integral)
