def total_do_semestre_por_bairro(todos):
    final = {}
    for bairro in todos:
        i = 6
        semestre = 0
        while i<12:
            semestre += todos[bairro][i]
            i += 1
        final[bairro] = semestre
    return final