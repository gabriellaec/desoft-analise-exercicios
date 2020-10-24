l=[1, 2, 3, -1, -2, -3, -4, 1]

i=0
def zera_negativos(z):
	n=len(z)
	while i<n:
		while l[i]<0:
			l[i]=0
		i+=1
    
print(zera_negativos(l))