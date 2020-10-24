def encontra_maximo(matriz):
   lista_maior_linha = []
   for lista in matriz:
        lista_maior_linha.append(max(  [abs(x) for x in lista]   ))
   return max(lista_maior_linha)
   
