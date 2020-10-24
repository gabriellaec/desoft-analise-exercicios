def conta_ocorrencias (texto):
    contagem = {}
    for palavra in texto:
        if not palavra in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem

 

def mais_frequente(texto):
    contagem = conta_ocorrencias(texto)
    maior = 0
    mais_frequente = ''
    for palavra, cont in contagem.items():
        if cont > maior:
            maior = cont
            mais_frequente = palavra
    return mais_frequente
    