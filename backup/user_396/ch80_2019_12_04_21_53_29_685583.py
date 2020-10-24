def interseccao_chaves(x, y):
   lista = []
   for e in x:
       for a in y:
           if x[e] == y[a]:
               lista.append(e)
               lista.append(a)
           
   return lista
