def junta_nome_sobrenome (lista1, lista2):
    nome = []
    n = 0
    i = 0
    while i < len(lista1):
        n = "{0} {1}".format(lista1[i],lista2[i])
        nome.append(n)    
        i += 1
    return(nome)