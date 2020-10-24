def primos_entres(a,b):
	x=0
	while a<=b:
		if a<2:
			a+=1
		elif a==2:
			a+=1
			x+=1
		elif a%2==0:
			a+=1
		else:
			d=3
			while a%d!=0 and a>d:
				d=d+2
			if a==d:
                x+=
				a+=1
	return x