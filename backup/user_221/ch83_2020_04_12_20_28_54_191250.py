d = {'Ana': 6,'Bibi': 5, 'Bulu': 6, 'Agu': 7, 'Bilu': 7, 'Abu': 8}
def medias_por_inicial(dicionario):
    lista = []
    contador = 0
    for nome, nota in dicionario.items():
        if lista == []:
            lista.append([])
            lista[contador].append(nome[0])
            lista[contador].append(1)
            lista[contador].append(nota)
            contador += 1
        else:
            k = 0
            for j in range(contador):
                if nome[0] == lista[j][0]:
                    lista[j][1] += 1
                    lista[j][2] = (lista[j][2]*(lista[j][1] - 1) + nota) / lista[j][1]
                    j += 1
                else:
                    k += 1
                    j += 1
            if k == contador:
                lista.append([])
                lista[contador].append(nome[0])
                lista[contador].append(1)
                lista[contador].append(nota)
                contador += 1

    novo_dicionario = {}
    i = 0
    for i in range(contador):
        novo_dicionario[lista[i][0]] = lista[i][2]
    return novo_dicionario