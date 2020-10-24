def subtracao_de_listas(a,b):
    lista=[]
    for variável in a:
        if not variável in b:
            lista.append(variável)
    return lista