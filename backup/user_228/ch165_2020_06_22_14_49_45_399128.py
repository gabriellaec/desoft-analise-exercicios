def mais_populoso(brasil):
    maiorpop=0
    maiorest=""
    for estado in brasil:
        i=0
        for municipio in brasil[estado]:
            i+=brasil[estado][municipio]
        if i>maiorpop:
            maiorpop=i
            maiorest=estado
    return maiorest