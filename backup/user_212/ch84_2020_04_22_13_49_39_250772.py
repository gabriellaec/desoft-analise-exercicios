def inverte_dicionario(pessoas_idades):
    saida={}
    for nome in pessoas_idades:  # o 'nome' é a chave do dicionário pessoas_idades
                                 #assim ele vai percorrer cada chave do dicionário
        if pessoas_idades[nome] not in saida:  # se a idade(valor do dicionario) não estiver em saida 
            saida[pessoas_idades[nome]]=[nome]
        elif pessoas_idades[nome]  in saida:
            saida[pessoas_idades[nome]].append(nome)  #adiciona nomes na lista nomeada para a chave nome(x)
                                                      # no dicionario saida 
    return saida