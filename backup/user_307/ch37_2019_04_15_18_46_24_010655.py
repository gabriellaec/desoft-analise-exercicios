n=123
def lista_primos(n):
	primos=[]
	h=1
	while h<=n:
		def eh_primo(h):
			primo=True
			i=1
			if h/2==1:
				primo=True
			elif h==0 or h==1:
				return False
			else:
				while i<h:
					if h%i==0 and i!=1:
						primo=False
					elif primo==False:
						i=h
					i+=1
			return primo
		if  eh_primo(h)==True:
			primos.append(h)
		h+=1
	return primos
print(lista_primos(n))
			