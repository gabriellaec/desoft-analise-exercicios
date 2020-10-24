def junta_nomes(homens, mulheres, sobrenomes):
    nomes_possiveis = []
    
    for i in range(len(homens)):
        for p in range(len(sobrenomes)):
            nomes_possiveis.append(homens[i] + ' ' + sobrenomes[p])
            
    for i in range(len(mulheres)):
        for p in range(len(sobrenomes)):
            nomes_possiveis.append(mulheres[i] + ' ' + sobrenomes[p])
    
    return nomes_possiveis