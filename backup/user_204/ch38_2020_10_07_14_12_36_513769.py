def quantos_uns(numero):
    i = 0
    ocorrencias = 0
    novo_numero = str(numero)
    while i < len(novo_numero):
        if numero[i] == 1:
            ocorrencias += 1
        i += 1
    return ocorrencias