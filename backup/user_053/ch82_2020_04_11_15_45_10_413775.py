# Define função pedida
def primeiras_ocorrencias(palavra):
    # Cria dicionário e listas
    dicionario_ocorrencias = dict()
    lista_caracteres = []
    posicao = []
    # Adiciona as diferentes letras e sua posição em suas respectivas listas
    i = 0
    for letra in palavra:
        if letra not in lista_caracteres:
            lista_caracteres.append(letra)
            posicao.append(i)
            i += 1
        else:
            i += 1
    # Cria dicionário com letras e primeira ocorrência
    for j in range(0, len(lista_caracteres)):
        dicionario_ocorrencias[lista_caracteres[j]] = posicao[j]
    # Retorna dicionário pedido
    return dicionario_ocorrencias