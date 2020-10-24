def mais_populoso(brasil):
    total=0
    for estados, cidades in brasil.items():
        habitantes=0
        for pop in cidades.values():
            habitantes+=pop
        if habitantes>total:
            habitantes=total
            mais_populos=estados
    return mais_populoso