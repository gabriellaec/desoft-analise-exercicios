def bairro_mais_custoso(empresa):
    semestral={}
    for bairro in empresa:
        semestral[bairro]=0
        for gasto in empresa[bairro][6:]:
            semestral[bairro]+=gasto

    maiorcusto=0
    nome="" 
    for k,v in semestral.items():
        if v>maiorcusto:
            maiorcusto=v
            nome=k
    return nome


            
            
            
            