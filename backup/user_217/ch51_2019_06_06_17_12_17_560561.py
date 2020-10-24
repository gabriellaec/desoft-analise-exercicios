

def estritamente_crescente(lista):
    lista_pos=[]
    i = 0
    maior = 0
      
    while i < len(lista):
        
        if lista[i] > maior :
            lista_pos.append(lista[i])
            maior = lista[i] 
        i = i + 1
        
    return lista_pos
