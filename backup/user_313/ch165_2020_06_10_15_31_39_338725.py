def mais_populoso(d1):
    soma = 0
    estados = dict()
    maior = list()
    maior.append(0)
    nome = list()
    nome.append(0)
    
    for k,v in d1.items():
        for t in v.values():
        
            soma += t
        estados[k] = soma 
      
    for c,r in estados.items():
        
        if r > maior[0]:
            maior[0] = r
            nome[0] = c
    
    return nome[0]   