# Define função
def conta_ocorrencias(lista):
    ocorrencias = {}
    # Verifica cada palavra
    for palavra in lista:
        contador = 0
        # Compara palavra anterior com todas da lista
        for palavra2 in lista:
            if palavra2 == palavra:
                contador += 1
        ocorrencias[palavra] = contador
    return ocorrencias