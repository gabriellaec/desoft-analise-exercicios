def verifica_preco(nome,dic,cor_preco):
    if nome in dic:
        cor = dic[nome]
        if cor in cor_preco:
            preco = cor_preco[cor]
            return preco