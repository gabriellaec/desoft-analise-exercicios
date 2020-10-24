def classifica_lista(lista):
    if len(lista)<2:
        return('nenhum')
    verificador_de_lista = lista[0] - lista[1]
    if verificador_de_lista == 0:
        return ('nenhum')
    elif verificador_de_lista < 0:
        i = 1
        while(i < range(len(lista)):
              if lista[i - 1] - lista[i] >= 0:
                  i += 1
                  return ('nenhum')
        return ('decrescente')
    if verificador_de_lista > 0:
        e = 1
        while(e < range(len(lista)):
              if lista[e - 1] - lista[e] <= 0:
                  e += 1
                  return ('nenhum')
        return ('crescente')
     