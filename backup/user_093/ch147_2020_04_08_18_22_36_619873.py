def conta_ocorrencias(lista):
    dicionario = {}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra]+=1
    return dicionario

             

def mais_frequente(lista2):
    ocorrencias=conta_ocorrencias(lista2)
    maior=0
    a_mais=''
    for a,oco in ocorrencias.items():
        if oco>maior:
            maior=oco
            a_mais=a
    return a_mais