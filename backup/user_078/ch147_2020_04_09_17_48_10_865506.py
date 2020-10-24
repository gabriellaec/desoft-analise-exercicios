def conta_ocorrencias(lista):
    dic={}
    for palavra in lista:
        dic[palavra] = lista.count(palavra)
    return dic

def mais_frequente(lista):
    dic=conta_ocorrencias(lista)
    
    comparador=0
    key=''
    for chave in dic:
        if dic[chave]>comparador:
            key = chave
            comparador = dic[chave]
    return key