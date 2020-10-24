def verifica_progressao(lista):
    i=0
    razaoPA=lista[i]-lista[i+1]
    razaoPG=lista[i]/lista[i+1]
    while i+2<len(lista):        
        if razaoPA==lista[i+1]-lista[i+2] and razaoPG==lista[i+1]/lista[i+2]:
            s='AG'
        elif razaoPA==lista[i+1]-lista[i+2]:
            s='PA'       
        elif  razaoPG==lista[i+1]/lista[i+2]:
            s='PG'
        else:
            s='NA'
        i+=1
    return s
      

       
            
        