def classifica_lista(lista):
    if len(lista)<2:
        return('nenhum')
    else:
        e = 0
        valor = True
        while(e < len(lista)):
            if lista[e] < lista[e + 1]:
                e += 1
            else:
                valor = False
                break
        if valor == True:
            return ('crescente')
        i = 0
        valor2 = True
        while(i < len(lista)):
            if lista[i] < lista[i + 1]:
                i += 1
            else:
                valor2 = False
                break
        if valor2 == True:
            return ('decrescente')
        else:
            return ('nenhum')