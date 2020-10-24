def bairro_mais_custoso(todos):
    maior_gasto = 0
    final = {}
    for bairro in todos:
        i = 6
        semestre = 0
        while i<12:
            semestre += todos[bairro][i]
            i += 1
        final[bairro] = semestre
        if final[bairro] > maior_gasto:
            maior_gasto = final[bairro]
            resposta = bairro
    return resposta