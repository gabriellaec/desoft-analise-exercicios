def conta_ocorrencias (lista):
    dicionario={}
    for palavra in lista:
        if palavra not in dicionario:
            dicionario[palavra]=1
        else:
            x=dicionario[palavra]+1
            dicionario[palavra]=x
    return dicionario

def mais_frequente (dic):
    maior=0
    for valor in dic.values():
        if valor>maior:
            maior=valor
    for chave,valor in dic.items():
        if valor==maior:
            maisfrequente=chave
    return maisfrequente