def junta_nome_sobrenome (nomes, sobrenomes):
    nomes_sobrenomse = []
    
    i = 0
    while i < len(nomes):
        nome_sobrenome = nomes[i] + " " + sobrenomes[i]
        
        nomes_sobrenomse.append(nome_sobrenome)
        
        i += 1
        
    return nomes_sobrenomse