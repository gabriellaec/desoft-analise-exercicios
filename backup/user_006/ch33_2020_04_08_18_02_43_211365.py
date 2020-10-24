def primos_entre(a,b):
    numero=a
    v=False
    nfinal=0
    while numero<=b:
        if numero==0 or numero==1:
	        v= False
        else:
            if numero==2:
			    v= True
		    else:
			    if numero%2==0:
				    v=False
			    else:
				    i=1
				    while i<(numero-1)/2:
					    if numero%(numero-2*i)==0:
						    v= False
					    else:
						    i=i+1
                    v= True
        if v==True:
            nfinal=nfinal+1
        numero=numero+1
    return nfinal