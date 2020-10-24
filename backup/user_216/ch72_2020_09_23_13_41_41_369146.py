def lista_caracteres(palavra):
    lista = []
    i = 0
    caractere = palavra[i]
    while i < len(palavra):
        caractere = palavra[i]
        if len(lista) == 0:
            lista.append(caractere)
        else:
            j = 0
            while j < len(lista):
                if caractere == lista[j]:
                    break
                else:
                    if j == len(lista) - 1:
                        lista.append(caractere)
                    else:
                        j += 1
        i += 1

    return lista