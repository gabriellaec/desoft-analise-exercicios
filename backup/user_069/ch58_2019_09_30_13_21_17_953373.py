def calcula_fibonacci (n):
	fibonacci=[0]*n
	fibonacci[0]=1
	fibonacci[1]=1
	i=2
	while i<(n-1):
    	fibonacci[i]=fibonacci[i-1]=fibonacci[i-2]
    	i=i+1
	print(fibonacci)  