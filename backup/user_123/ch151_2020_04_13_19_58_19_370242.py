def classifica_lista(lista): 
    if 2 > len(lista):
        return "nenhum"
    
   for e in lista:
       if lista == sorted(lista):
           return "crescente"
        elif lista == sorted(lista, reverse=True):
            return "decrescente"
        elif lista != sorted(lista) and sorted(lista, reverse=True):
            return "nenhum" 