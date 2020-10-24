def numero_no_indice (lista):
   i = 0
   lista2 = []
   while i < len(lista):
       if lista [i] == i:
           lista2.append(lista[i])
           i = i + 1
       else:
           i = i + 1
   return lista2 