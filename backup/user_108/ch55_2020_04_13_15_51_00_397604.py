def encontra_maximo(matriz):
   lista_maior_linha = []
   for lista in matriz:
        lista_maior_linha.append(max(lista))
   return max(lista_maior_linha)
   
    