def mais_populoso (brasil):
    pes=0
    for estado in brasil:
        for pop in estado:
            k=estado[pop]
            pes+=k
    populoso=pes