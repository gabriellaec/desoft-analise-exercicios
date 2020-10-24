def conta_ocorrencias (lista):
    dic = {}
    for palavra in lista:
        if not palavra in dic:
            dic [palavra] = 1
        else:
            dic [palavra] += 1
    return dic 
            
def mais_frequente(lista):
    dic = conta_ocorrencias(lista)

    palavra_mais_frequente = ''
    maior_frequencia = 0

    for palavra, ocorrencias in dic.items():
        if ocorrencias > maior_frequencia:
            maior_frequencia = ocorrencias
            palavra_mais_frequente = palavra
    return palavra_mais_frequente
        