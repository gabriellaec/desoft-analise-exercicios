def lista_primos(n):
    lista=[]*n
    g=0
    while g<n:
	    if g==0 or g==1:
		    return False
        else:
            if g==2:
                return True
            else:
                if g%2==0:
			    	return False
                else:
			    	i=1
			    	while i<(g-1)/2:
				    	if g%(g-2*i)==0:
						    return False
                        else:
					    	i=i+1
				    return True
        if True:
            lista.append(g)
        g=g+1
    return lista