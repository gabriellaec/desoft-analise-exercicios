def classifica_lista(lista_entrada):

    if len(lista_entrada) < 2:
        return "nenhum"

    for elemento in lista_entrada:
        if lista_entrada == sorted(lista_entrada):
            return "crescente"
        elif lista_entrada == sorted(lista_entrada, reverse = True):
            return "decrescente"
        elif lista_entrada != sorted(lista_entrada) and lista_entrada != sorted(lista_entrada, reverse = True):
            return "nenhum"
 