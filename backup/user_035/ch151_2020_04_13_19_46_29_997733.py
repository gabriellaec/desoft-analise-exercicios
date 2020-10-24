def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    else:
        i = 0
        while i <= len(lista)-1:
            if lista[i]>lista[i+1]:
                return "decrescente"
            elif lista[i]<lista[i+1]:
                return "crescente"
            else:
                return "nenhum"