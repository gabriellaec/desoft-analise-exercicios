def mais_populoso(dicionario_pais):
    estado_mais_populoso = ""
    maior_população = 0

    for estado in dicionario_pais:
        contador = 0
        for municipio in dicionario_pais[estado]:
            contador += dicionario_pais[estado][municipio]
        
        if contador >= maior_população:
            maior_população = contador
            estado_mais_populoso = estado 
    
    return estado_mais_populoso