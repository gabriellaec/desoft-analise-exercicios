from collections import Counter
def primeiras_ocorrencias(string):
    l=Counter(string)
    posicoes=[]
    chavess=l.keys()
    for chave in l: 
        y=string.find(chave)
        posicoes.append(y)
    r=dict(zip(chavess,posicoes))
    return r
        
    