

def mais_frequente (lista_palavras):
    
    def conta_ocorrencias (lista_palavras):
        palavra_ocorrencia = {}
        for i in lista_palavras:
            if i not in palavra_ocorrencia:
                palavra_ocorrencia[i] = 1
            else:
                palavra_ocorrencia[i] +=1
        return palavra_ocorrencia
    
    palavra_ocorrencia = conta_ocorrencias(lista_palavras)
    
    for i in palavra_ocorrencia:
        for j in palavra_ocorrencia:
            
            if palavra_ocorrencia[i]>palavra_ocorrencia[j]:
                maior_ocorrencia = i
    return i
        