def monta_dicionario(lista_chave,lista_valor):
    dic={}
    cont=0
    while cont<len(lista_valor) and cont<len(lista_chave):
        for v in lista_chave:
            dic[v]=lista_valor[cont]
            cont+=1
    return dic