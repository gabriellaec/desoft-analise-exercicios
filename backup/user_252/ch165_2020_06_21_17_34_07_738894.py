def mais_populoso (brasil):
    pessoas=0
    for estados, cidades in brasil.items():
        total=0
        for pop in cidades:
            k=estado[pop]
            total+=k
        if total>pessoas:
            pessoas=total
            mais_populosa=estados
    return mais_populosa