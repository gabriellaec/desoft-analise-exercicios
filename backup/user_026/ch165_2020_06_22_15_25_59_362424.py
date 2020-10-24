def mais_populoso(dicionario):
    estados = {}
    for estado, municipios in dicionario.items():
        total = 0
    for municipio in municipios.values():
        total += municipio
        estados[estado] = total
        maior_estado = ""
        maior_populacao = 0
    for estado, populacao in estados.items():
        if populacao > maior_populacao:
            maior_populacao = populacao
            maior_estado = estado
    return maior_estado
brasil = {"São Paulo":{"São Paulo":21571281,"Campinas":3224443},
        "Minas Gerais":{"Belo Horizonte":2385639,"Uberlândia":611903}}
print(mais_populoso(brasil))