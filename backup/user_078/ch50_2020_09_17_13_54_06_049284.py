#como colocar um espaço?
def junta_nome_sobrenome(lista_nomes, lista_sobrenomes):
    lista_completos = []
    i = 0

    while i < len(lista_nomes):
        completo = lista_nomes[i] + lista_sobrenomes[i]
        lista_completos.append(completo)
        i += 1
    
    return lista_completos