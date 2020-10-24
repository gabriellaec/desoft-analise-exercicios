# Conta ocorrência de cada palavra
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

# Define função pedida
def mais_frequente(lista2):
    dict_ocorrencias = conta_ocorrencias(lista2)  # Devolve dicionário com ocorrências de cada palavra
    for palavra, contagem in dict_ocorrencias.items():
        # Identifica palavra com contagem máxima
        if contagem == max(dict_ocorrencias.values()):
            return palavra