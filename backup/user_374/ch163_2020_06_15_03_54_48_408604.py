def calcula_media(lista_dicionarios):
    var_soma = 0
    var_contagem = 0
    for d in lista_dicionarios:
        for k in d:
            var_soma += d[k]
            var_contagem += 1
    
    return var_soma/var_contagem
    