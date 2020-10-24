
l1 = ['flamengo','palmeiras','santos']
l2 = ['lider','vice-lider','terceiro']

def monta_dicionario(l1,l2):
    dici = {}
    for i in range(len(l1)):
        dici[l1[i]]=l2[i]
    return dici
print(monta_dicionario(l1,l2))    