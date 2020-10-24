def mais_populoso(pais):
    maiorpop=0
    maiorest=""
    i=0
    for estado in pais:
        for municipio in pais[estado]:
            i+=pais[estado][municipio]
        if i>maiorpop:
            maiorpop=i
            maiorest=estado
    return maiorest