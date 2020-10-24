def bairro_mais_custoso(empresa):
    semestral={}
    for bairro in empresa:
        semestral[bairro]=0
        for gasto in empresa[bairro][6:]:
            semestral[bairro]+=gasto

    maiorcusto=0
    nome="" 
    for bairro,custo in semestral.items():
        if custo>maiorcusto:
            maiorcusto=custo
            nome=bairro
    return nome


            
            
            
            