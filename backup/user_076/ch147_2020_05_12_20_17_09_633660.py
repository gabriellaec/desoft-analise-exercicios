

def mais_frequente (lista_palavras):
    
    def conta_ocorrencias (lista_palavras):
        palavra_ocorrencia = {}
        for i in lista_palavras:
            if i not in palavra_ocorrencia:
                palavra_ocorrencia[i] = 1
            else:
                palavra_ocorrencia[i] +=1
        return palavra_ocorrencia
    
    palavra_ocorrência = {}
    palavra_ocorrência = conta_ocorrencias(lista_palavras)
    
    for i in palavra_ocorrência:
        frequência = 0
        if palavra_ocorrência [i] > frequência:
            mais_frequente = i
            frequência = palavra_ocorrência[i]
        
    return mais_frequente
        