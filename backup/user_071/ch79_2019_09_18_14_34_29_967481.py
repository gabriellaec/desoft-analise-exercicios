lista1=('domingo', 'segunda', 'terca', 'quarta')
lista2=(1, 2, 3, 4)
def monta_dicionario(x, y):
    i=0
    alfa={}
    while i<len(x):
        alfa[x[i]]=y[i]
        i+=1
    return alfa
