def verifica_primos(listanum):
    dicionario={}
    for n in listanum:
        if n==0 or n==1:
            dicionario[n]=False
        elif n==2:
            dicionario[n]=True
        else:
            if n%2==0:
                dicionario[n]=False
            else:
                d=3
                while n>d:
            	    if n%d==0:
                	    dicionario[n]=False
                        break
            	    else:
                	    d+=2
                dicionario[n]=True
    return dicionario
        