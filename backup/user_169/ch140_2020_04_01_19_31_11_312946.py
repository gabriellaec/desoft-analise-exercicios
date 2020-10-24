lista=[2,4,6,8]
def faixa_notas(lista):    
    i=0
    lista2=[]
    
    while i<len(lista):
        if lista[i]<5:
            lista2.append(len(lista[i]<5))
            
        if lista[i]>=5 and lista[i]<=7:
            lista2.append(len(lista[i]>=5 and lista[i]<=7))
            
        if lista[i]>7:
            lista2.append(len(lista[i]>7))      
        i+=1
        
            
       
            