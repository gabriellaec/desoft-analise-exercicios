def mais_populoso(estados_brasil):
    maior_populacao = 0;
    estado_mais_populoso = "";

    for estado, cidades in estados_brasil.items():
        soma_populacao = 0;

        for cidade, populacao in cidades.items():
            soma_populacao = soma_populacao + populacao
        if (soma_populacao > maior_populacao):
            maior_populacao = soma_populacao
            estado_mais_populoso = estado

    print("Estado mais populoso é", estado_mais_populoso, "com", maior_populacao, "habitantes")


brasil = {"São Paulo": {"São Paulo": 21571281, "Campinas": 3224443},
          "Minas Gerais": {"Belo Horizonte": 2385639, "Uberlândia": 611903},
          "Rio de Janeiro": {"Rio de Janeiro": 6718903, "São Gonçalo": 1084839},
          "Paraná": {"Curitiba": 1917185, "Londrina": 563943}}

mais_populoso(brasil)