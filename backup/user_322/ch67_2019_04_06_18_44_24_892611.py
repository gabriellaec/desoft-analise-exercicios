def aluno_impares(n):
    lista = []
    for i in range(0,len(n)):
        if i % 2 != 0:
            lista.append(n[i])
    return lista