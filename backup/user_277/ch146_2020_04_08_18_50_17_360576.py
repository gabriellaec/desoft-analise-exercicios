def conta_ocorrencias(lista_1):
    dicionario={i:lista_1.count(i) for i in lista_1}
    return dicionario