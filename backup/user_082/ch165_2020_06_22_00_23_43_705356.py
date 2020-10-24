def mais_populoso(pais):
    maior_estado = 0
    nome_maior_estado = ''

    for estado in pais:
        populacao = 0

        for cidade in pais[estado]:
            populacao += pais[estado][cidade]

            if populacao > maior_estado:
                maior_estado = populacao
                nome_maior_estado = estado
    return nome_maior_estado