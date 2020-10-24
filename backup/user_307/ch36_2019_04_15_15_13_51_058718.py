def eh_primo(n):
	primo=True
	i=1
	if n/2==1:
		primo=True
	elif n==0:
		return False
	else:
		while i<n:
			if n%i==0 and i!=1:
				primo=False
			elif primo==False:
				i=n
			i+=1
	return primo
print(eh_primo(0))