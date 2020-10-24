def mais_populoso (brasil):
    lista_populacoes = []
    somatoria_estado = 0
    for estado in brasil:
        for populacao in estado.values():
            for numeros in populacao.values():
                somatoria_estado += numeros

        lista_populacoes.append(somatoria_estado)
    
    maior_valor = max(lista_populacoes)

    for maior_valor in populacao
                