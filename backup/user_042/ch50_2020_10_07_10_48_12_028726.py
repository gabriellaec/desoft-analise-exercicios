def junta_nome_sobrenome(nome, sobrenomes):
    i = 0
    y = []
    while i < len(nome):
        z = nome[i] + ' '+ sobrenomes[i]
        y.append(z)
        i =i+ 1
    return y
    
    