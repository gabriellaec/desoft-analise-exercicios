def estritamente_crescente (lista):
    i=0

    novalista=[]
    while i < len(lista):
     
        if lista[ i ]<= lista[i+1]:
            maiorlista=lista[i+1]
            novalista.append(lista[i])
        i+=1 


        
         
        
        
        