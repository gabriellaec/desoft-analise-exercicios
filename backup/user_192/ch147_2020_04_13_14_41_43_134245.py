
def conta_ocorrencias(palavras):
    contagem={}
    for palavra in palavras:
        if not palavra in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem

def mais_frequentes(palavras):
    dicionario = conta_ocorrencias(palavras)
    ocorrencias = list()
    for ocorrencia in dicionario.values():
        ocorrencias.append(int(ocorrencia))
    maior_ocorrencia = max(ocorrencias)
    for p in dicionario:
        if dicionario[p] == maior_ocorrencia:
            return p
    
        
        
    