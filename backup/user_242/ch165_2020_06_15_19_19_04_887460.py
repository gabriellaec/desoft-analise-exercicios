def mais_populoso(pais):
    maior_estado = ""
    maior_populacao = 0
    
    for estado in pais:
        contador = 0
        for municipio in pais[estado]:
            contador = contador + pais[estado][municipio]
        if contador > maior_populacao:
            maior_populacao = contador
            maior_estado = estado
    return maior_estado


brasil = {
    "São Paulo": {"São Paulo": 21571281, "Campinas": 3224443},
    "Minas Gerais": {"Belo Horizonte": 2385639, "Uberlândia": 611903},
}  

print(mais_populoso(brasil))