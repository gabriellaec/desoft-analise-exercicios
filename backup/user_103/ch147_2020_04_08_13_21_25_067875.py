def conta_ocorrencias(lista):
    dicionario={}
    i=0
    for i in lista:
        if not i in dicionario:
            dicionario[i]=1
        else:
            dicionario[i]+=1
 
    return dicionario

def mais_frequente(lista2):
    ocorrencias=conta_ocorrencias(lista2)
    maior_ocorrencia=0
    palavra_mais_frequente=''
    for palavra in ocorrencias.items():
        if palavra > maior_ocorrencia:
            maior_ocorrencia=palavra.value
            palavra_mais_frequente= palavra.key
        print(palavra_mais_frequente)
    