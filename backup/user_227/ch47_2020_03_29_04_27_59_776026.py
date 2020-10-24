def estritamente_crescente(lista):
    i = 0
    lista_crescente = []
    while i < len(lista):
        if i == 0:
            lista_crescente.append(lista[i])
            i += 1
        
        elif lista[i] <= lista[0]:
            i += 1
        
        else:
            condicao = True
            a = 1
            while i-a != 0 and condicao:
                if lista[i] > lista[i-a]:
                    a += 1            
                
                else:
                    condicao = False
            
            if i - a == 0:
                lista_crescente.append(lista[i])
                i += 1
           
            else:
                i += 1
    
    return lista_crescente