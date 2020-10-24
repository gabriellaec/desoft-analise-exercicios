def verifica_progressao (lista):
    i = 0
    while i < (len(lista)-2):
        if lista[i] == 2*lista[i + 1] - lista[i + 2]:
            return '"PA"'
        if lista[i] == (lista[i +1]**2) * lista[i + 2]:
            return '"PG"'
        if lista[i] == 2*lista[i + 1] - lista[i + 2] and lista[i] == (lista[i +1]**2) * lista[i + 2]:
            return '"AG"'
        else:
            return '"NA"'
        i = i + 1
        
        