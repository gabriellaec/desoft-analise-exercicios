def verifica_primos(lista):
    dicio={}
    g=0
    v=False
    while g<len(lista):
        numero=lista[i]
	    if numero==0 or numero==1:
		    v= False
	    else:
		    if numero==2:
			    v= True
		    else:
			    if numero%2==0:
				    v= False
			    else:
			    	i=1
				    while i<(numero-1)/2:
					    if numero%(numero-2*i)==0:
					    	v= False
					    else:
					    	i=i+1
				    v= True
        if v==True:
            dicio[numero]=True
        else:
            dicio[numero]=False
        g=g+1	