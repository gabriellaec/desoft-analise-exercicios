def junta_nome_sobrenome(lista_nome,lista_sobrenome):
    pessoa = []
    i = 0
    for e in lista_nome:
        pessoa.append(e + " " + lista_sobrenome[i])
        i += 1
    return pessoa
    