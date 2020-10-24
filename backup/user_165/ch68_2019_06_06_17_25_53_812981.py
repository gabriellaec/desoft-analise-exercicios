def separa_trios(lista_aluno):
    lista_trio = []
    for i in lista_aluno:
        i = 0
        x = lista_aluno[:i+3]
        lista_trio.append(x)