def verifica_preco(nomeli, dicionome, diciocor):
    
    tituloli = list(dicionome.keys())
    
    nomelivro = list(diciocor.keys())
    
    valorcor = list(dicionome.values())
    
    valorlivro = list(diciocor.values())
    
    for i in range(len(valorlivro)):
        if valornome == nomelivro[i]:
            return valorlivro[i]
        
    for i in range(len(tituloli)):
        if nomeli == tituloli[i]:
            valornome = valorcor[i]
            break
            
    corlivro = valorcor[i]