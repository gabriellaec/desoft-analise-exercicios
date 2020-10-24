def lista_primos(n):
    i=1
    lista=[]
    while i<n:
         if n==2:
            lista.append(i)
            return lista
        else:
            if n%2==0:
                return lista
            else:
                d=3
                while n>d:
            	    if n%d==0:
                	    return lista
            	    else:
                	    d+=2
    return lista