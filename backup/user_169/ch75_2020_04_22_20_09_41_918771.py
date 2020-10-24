def verifica_primos(lista):
    dicionario={}

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
                n=3
                while n<i:
                    if i%n==0:
                        dicionario[i]=False
                        break
                    else:
                        n+=2
                       
                        
    return dicionario
                        
                    
                
                
            