def verifica_progressao(lista):
    i=0
    razaoPA=lista[i]-lista[i+1]
    razaoPG=lista[i]/lista[i+1]
    while i+2<len(lista):        
        if razaoPA==lista[i+1]-lista[i+2] and razaoPG==lista[i+1]/lista[i+2]:
            return'AG'
        elif razaoPA==lista[i+1]-lista[i+2]:
            return'PA'       
        elif  razaoPG==lista[i+1]/lista[i+2]:
            return'PG'
        else:
            return'NA'
        i+=1

      

       
            
        