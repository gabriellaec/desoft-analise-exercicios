def conta_ocorrencias(lista):
    dicionario= {i:lista.count(i) for i in lista}
    return dicionario