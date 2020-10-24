def alunos_impares(nomes):
    new = []
    i = 1
    while i <= (len(nomes)-1):
        a = nomes[i]
        new.append(a)
        i += 2
    return new
        
        