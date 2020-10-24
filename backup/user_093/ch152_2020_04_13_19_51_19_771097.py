def verifica_preco(titulo,nome,preco):
    for i in nome:
        if i==titulo:
            cor= nome[i]
    for a in preco:
        if a==cor:
            valor=preco[a]
    return valor