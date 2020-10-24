def lista_primos(n):
    lista=[]
    cont=0
    while cont<=n:
    	for num in range (2,n):
       		primo=True
      		for e in range (2,n):
            	if num%e==0:
                	primo=False
        if primo==True:
            lista.append(num)
            cont+=1
    return lista