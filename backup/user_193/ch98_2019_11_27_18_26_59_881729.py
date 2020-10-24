def bairro_mais_custoso(dicionario):
    dic=total_do_semestre_por_bairro(dicionario)
    valores=list(dic.values)
    maior=max(valores)
    chave=dic.get(None[maior])
    return chave