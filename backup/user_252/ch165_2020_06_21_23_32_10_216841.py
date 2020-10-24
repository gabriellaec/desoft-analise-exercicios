def mais_populoso(brasil):
    total=0
    for estados, cidades in brasil.items():
        habitantes=0
        for pop in cidades.values():
            habitantes+=pop
        if habitantes>total:
            total=habitantes
            mais_populoso=estados
    return mais_populoso