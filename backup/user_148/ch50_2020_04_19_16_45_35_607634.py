def junta_nome_sobrenome(nome, sobrenome):
    l2 = []
    i = 0
    
    while i<len(nome):
        l2.insert(i, nome[i], end='')
        i += 1
    while i<len(sobrenome):
        l2.insert(i, sobrenome[i])
        i += 1
        
    return l2