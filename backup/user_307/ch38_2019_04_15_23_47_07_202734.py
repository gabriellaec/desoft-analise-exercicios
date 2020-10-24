a=2
b=16
def primos_entre(a,b):
	n=a
	i=0
	while n<=b:
		def eh_primo(n):
			primo=True
			i=1
			if n/2==1:
				primo=True
			elif n==0 or n==1:
				return False
			else:
				while i<n:
					if n%i==0 and i!=1:
						primo=False
					elif primo==False:
						i=n
					i+=1
			return primo
		if eh_primo(n)==True:
			i+=1
		n+=1
	return i
print (primos_entre(a,b))