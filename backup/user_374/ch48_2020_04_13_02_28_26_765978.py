def eh_crescente(lista):
    if len(lista) == 0:
        return False
    i = 1
    teste = True
    while i < len(lista):
       if lista[i-1] < lista[i]:
           if i == len(lista) -1:
               teste = True
           else: 
               i += 1
       else:
            teste = False
  
    return teste
