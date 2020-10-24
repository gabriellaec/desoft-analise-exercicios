
def conta_ocorrencias(palavras):
    contagem = {}
    for word in palavras:
        if not word in contagem:
            contagem[word] = 1
        else:
            contagem[word] +=1
    return contagem

def mais_frequente(palavras):
    contagem = conta_ocorrencias(palavras)
    for c,v in contagem.items:
        if v == max(contagem):
            maisAparece = 'c'
    return maisAparece
            
        
        