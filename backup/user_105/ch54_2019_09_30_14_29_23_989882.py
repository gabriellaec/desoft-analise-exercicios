def junta_nome_sobrenome(lista_nomes,lista_sobrenomes):
    lista_nome_e_sobrenome = []
    for i in range(len(lista_nomes)):
        nome = lista_nomes[i]+' '+lista_sobrenomes[i]
        lista_nome_e_sobrenome.append(nome)
        
    return lista_nome_e_sobrenome