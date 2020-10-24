

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
        mais_frequente = 0
        if palavra_ocorrência [i] > frequência:
            mais_frequente = palavra_ocorrência[i]
            frequência = i
        
    return mais_frequente
        