def inverte_dicionario(dic):
    novo_dic={}
    for chave,valor in dic:
        if valor in novo_dic:
            novo_dic[valor].append(chave)
        else:
            novo_dic[valor]=[chave]
         