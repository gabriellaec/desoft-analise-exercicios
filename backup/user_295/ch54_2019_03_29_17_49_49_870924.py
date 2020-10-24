def junta_nome_sobrenome(lista_nome, lista_sobrenome):
    i = 0 
    lista = []
    while i < len (lista_nome):
        string = lista_nome[i] + " " + lista_sobrenome[i]
        lista.append (string)
        i += 1
    return lista 