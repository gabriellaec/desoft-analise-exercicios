def mais_populoso(dicionario):
    lista_compara = []
    dici = {}
    #Primeiro loop para chegar aos valores e adicionar a soma deles em outro dicionário.
    for keys,dic in dicionario.items():
        total = sum(dic.values())
        dici[keys] = total

    #Adicionando a soma em uma lista para pegar o valor máximo de uma vez só 
    lista = list(dici.values())
    for chave,valores in dici.items():
        #Se o máximo da lista for igual a uma dos valores(soma) retorna a key!
        if max(lista) == valores:
            return chave
