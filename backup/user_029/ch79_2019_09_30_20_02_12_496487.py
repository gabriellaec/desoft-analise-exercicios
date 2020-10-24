
l1 = ['flamengo','palmeiras','santos']
l2 = ['lider','vice-lider','terceiro']

def monta_dicionario(l1,l2):
    dici = {}
    for k in range(len(l1)):
        dici[l1[k]]=l2[k]
    return dici
print(monta_dicionario(l1,l2))    