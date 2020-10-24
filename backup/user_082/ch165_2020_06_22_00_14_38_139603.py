def mais_populoso(estados):
    maior_estado = 0
    nome_maior_estado = 0
    
    for estado in estados:
        populacao = 0
        for cidade in estado:
            populacao += estados[estado[cidade]]

            if populacao > maior_estado:
                maior_estado = populacao
                nome_maior_estado = estado
    return nome_maior_estado