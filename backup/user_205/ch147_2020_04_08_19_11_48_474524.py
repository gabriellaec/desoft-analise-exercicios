def conta_ocorrencias(lista): 
    dic={}
    for palavras in lista:
        dic[palavras]=lista.count(palavras)
    return dic
def mais_frequente(lista2):
    dic = conta_ocorrencias(lista2)
    y = 0
    palavra = " "
    for chave,valor in dic.items():
        if valor > y : 
            y=valor 
            palavra = chave 
            
    return palavra
            