def junta_nome_sobrenome(lista1,lista2):
    nomes= lista1+lista2
    n = [nome.strip().split(' ')[0] for nome in nomes ]
    return n

    