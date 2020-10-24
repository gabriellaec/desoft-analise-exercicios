def junta_nome_sobrenome(n,s):
    tamanho_um = len(n)
    tamanho_dois = len(s)
    lista_nomes = [0]*tamanho_um
    espaço = ' '
    i = 0
    while i < (tamanho_um) and i < (tamanho_dois):
        lista_nomes[i] = n[i] + espaço + s[i]
        i += 1
    return lista_nomes