def verifica_primos(listanum):
    dicionario={}
    for n in listanum:
        if n==-1 or n==0 or n==1:
            dicionario[n]=False
        elif n==2:
            dicionario[n]=True
        else:
            dicionario[n]=True
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
    return dicionario
        