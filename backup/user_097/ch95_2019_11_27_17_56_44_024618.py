brasil = {"São Paulo":{"São Paulo":21571281,"Campinas":3224443},
          "Minas Gerais":{"Belo Horizonte":2385639,"Uberlândia":611903}}


def mais_populoso(dicionario_pais):

    lista_estados = []
    lista_populacoes = []

    for estado in brasil:
        lista_estados.append(estado)

    for estado in brasil:

        dict_estado = (brasil[estado])

        pop_total = 0

        for populacao in dict_estado.values():
            pop_total = pop_total + populacao

        lista_populacoes.append(pop_total)

    maior_populacao = max(lista_populacoes)
    indice_maior_populacao = lista_populacoes.index(maior_populacao)

    return lista_estados[indice_maior_populacao]

print(mais_populoso(brasil))