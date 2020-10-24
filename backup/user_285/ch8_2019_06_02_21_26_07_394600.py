def verifica_progressao(lista):
    i=0
    x=lista[i]-lista[i+1]
    y=lista[i]/lista[i+1]
    while i+2<len(lista):        
        if x==lista[i+1]-lista[i+2] and y==lista[i+1]/lista[i+2]:
            s='AG'
        elif x==lista[i+1]-lista[i+2]:
            s='PA'       
        elif  y==lista[i+1]/lista[i+2]:
            s='PG'
        else:
            s='NA'
        i+=1
    return s
      

       
            
        