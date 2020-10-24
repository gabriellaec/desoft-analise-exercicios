def junta_nome_sobrenome (nomes, sobrenome):
    lista_nome_e_sobrenome=[]
    contador = 0
    while contador <len(nomes):
        lista_nome_e_sobrenome.append("{} {}".format(nomes[contador], sobrenome[contador]))
        contador +=1
    return lista_nome_e_sobrenome    