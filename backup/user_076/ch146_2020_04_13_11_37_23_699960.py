def conta_ocorrencias (lista_palavras):
    palavra_ocorrencia = {}
    for i in lista_palavras:
        if i not in palavra_ocorrencia:
            palavra_ocorrencia[i] = 1
        else:
            palavra_ocorrencia[i] +=1
    return palvra_ocorrencia
        