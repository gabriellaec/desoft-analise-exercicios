from math import factorial 
def euler(x,n):
    a = 0
    soma = 0
    while a<n:
        soma += (x**a)/(factorial(a))
		a += 1
	return soma