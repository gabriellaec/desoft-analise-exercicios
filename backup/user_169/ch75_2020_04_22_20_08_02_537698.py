def verifica_primos(lista):
    dicionario={}
    n=3
    for i in lista:
        if i==0 and i==1 and i==-1:
            dicionario[i]=False
        
        elif  i==2:
             dicionario[i]=True
        
        else:
            dicionario[i]=True
            if i%2==0:
                dicionario[i]=False
            else:
                while n<i:
                    if i%n==0:
                        dicionario[i]=False
                        n+=2
                        
    return dicionario
                        
                    
                
                
            