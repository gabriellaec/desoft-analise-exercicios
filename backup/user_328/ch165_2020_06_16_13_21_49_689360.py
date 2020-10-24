def mais_populoso(pais):
    maior_estado= ""
    maior_populacao= 0
    for estado in pais:
        contador = 0
        for municipio in pais[estado]:
            contador += pais[estado][municipio]
        if contador > maior_populacao:
            maior_populacao = contador
            maior_estado = estado
            
    return maior_estado

#brasil = {"São Paulo":{ "São Paulo": 4938427, "Campinas": 8197 },
# "Minas Gerais": { "Belo Horizonte": 589873, "Uberlândia": 99390  }}
#print(mais_populoso(brasil))